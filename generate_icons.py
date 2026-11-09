import os
from PIL import Image, ImageDraw, ImageFilter

def create_gemini_icon(size):
    # Create image with RGBA
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Rounded background rectangle or full square (iOS rounds it automatically)
    # Slate gradient: from #0F172A (top-left) to #1E293B (bottom-right) with slate-blue tint
    top_color = (15, 23, 42)     # #0F172A
    bot_color = (30, 41, 59)     # #1E293B
    accent_glow = (59, 130, 246) # #3B82F6
    
    # Draw vertical gradient
    for y in range(size):
        ratio = y / float(size)
        r = int(top_color[0] * (1 - ratio) + bot_color[0] * ratio)
        g = int(top_color[1] * (1 - ratio) + bot_color[1] * ratio)
        b = int(top_color[2] * (1 - ratio) + bot_color[2] * ratio)
        draw.line([(0, y), (size, y)], fill=(r, g, b, 255))
        
    # Draw subtle slate-blue radial ambient glow in the center
    center_x, center_y = size / 2.0, size / 2.0
    glow_radius = size * 0.42
    
    # Create an overlay for glow
    glow_img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow_img)
    
    for r_cur in range(int(glow_radius), 0, -3):
        alpha = int(35 * (1.0 - r_cur / glow_radius))
        glow_draw.ellipse(
            [center_x - r_cur, center_y - r_cur, center_x + r_cur, center_y + r_cur],
            fill=(accent_glow[0], accent_glow[1], accent_glow[2], alpha)
        )
    img = Image.alpha_composite(img, glow_img)
    draw = ImageDraw.Draw(img)

    # Draw Gemini Star (four-point sparkle / diamond curve)
    # Parametric 4-pointed star curve (astroid / superellipse: x^(2/3) + y^(2/3) <= r^(2/3))
    star_radius = size * 0.28
    points = []
    num_pts = 180
    import math
    for i in range(num_pts):
        angle = 2.0 * math.pi * i / num_pts
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        
        # Astroid / star formula: x = r * cos^3(t), y = r * sin^3(t)
        # We mix with circle for smooth organic curve
        px = center_x + star_radius * (math.pow(abs(cos_a), 2.5) * (1 if cos_a >= 0 else -1))
        py = center_y + star_radius * (math.pow(abs(sin_a), 2.5) * (1 if sin_a >= 0 else -1))
        points.append((px, py))
        
    # Draw star filled with vibrant slate-blue to cyan gradient
    star_img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    star_draw = ImageDraw.Draw(star_img)
    star_draw.polygon(points, fill=(255, 255, 255, 255))
    
    # Apply gradient to star
    star_grad = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(star_grad)
    for y in range(int(center_y - star_radius), int(center_y + star_radius) + 1):
        if y < 0 or y >= size:
            continue
        rel = (y - (center_y - star_radius)) / (star_radius * 2.0)
        # From Electric Blue (#60A5FA) to Indigo (#818CF8) to Cyan (#38BDF8)
        cr = int(96 * (1 - rel) + 56 * rel)
        cg = int(165 * (1 - rel) + 189 * rel)
        cb = int(250 * (1 - rel) + 248 * rel)
        s_draw.line([(0, y), (size, y)], fill=(cr, cg, cb, 255))
        
    # Mask star gradient with star polygon
    star_layer = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    star_layer.paste(star_grad, (0, 0), mask=star_img)
    
    # Outer star glow
    blur_star = star_img.filter(ImageFilter.GaussianBlur(radius=size * 0.03))
    glow_tint = Image.new("RGBA", (size, size), (96, 165, 250, 140))
    glow_final = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    glow_final.paste(glow_tint, (0, 0), mask=blur_star)
    
    img = Image.alpha_composite(img, glow_final)
    img = Image.alpha_composite(img, star_layer)
    
    # Small satellite diamond star at top-right
    s2_cx = center_x + star_radius * 0.75
    s2_cy = center_y - star_radius * 0.75
    s2_r = star_radius * 0.32
    pts2 = []
    for i in range(num_pts):
        angle = 2.0 * math.pi * i / num_pts
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        px = s2_cx + s2_r * (math.pow(abs(cos_a), 2.5) * (1 if cos_a >= 0 else -1))
        py = s2_cy + s2_r * (math.pow(abs(sin_a), 2.5) * (1 if sin_a >= 0 else -1))
        pts2.append((px, py))
        
    sat_img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    sat_draw = ImageDraw.Draw(sat_img)
    sat_draw.polygon(pts2, fill=(192, 222, 255, 230))
    img = Image.alpha_composite(img, sat_img)
    
    # Convert RGBA to RGB for standard iOS AppIcon
    final_rgb = Image.new("RGB", (size, size), (15, 23, 42))
    final_rgb.paste(img, (0, 0), mask=img)
    return final_rgb

def main():
    out_dir = r"C:\Users\vasil\OneDrive\Рабочий стол\gemini lite\GeminiLite\Assets.xcassets\AppIcon.appiconset"
    os.makedirs(out_dir, exist_ok=True)
    
    sizes = [
        ("icon_1024.png", 1024),
        ("icon_180.png", 180), # iPhone @3x (60pt)
        ("icon_120.png", 120), # iPhone @2x (60pt) & @3x (40pt)
        ("icon_87.png", 87),   # iPhone @3x (29pt settings)
        ("icon_80.png", 80),   # iPhone @2x (40pt spotlight)
        ("icon_60.png", 60),   # iPhone @3x (20pt notification)
        ("icon_58.png", 58),   # iPhone @2x (29pt settings)
        ("icon_40.png", 40),   # iPhone @2x (20pt notification)
    ]
    
    base_1024 = create_gemini_icon(1024)
    base_1024.save(os.path.join(out_dir, "icon_1024.png"), "PNG")
    print("Saved 1024x1024 base icon")
    
    for filename, sz in sizes:
        if sz == 1024:
            continue
        resized = base_1024.resize((sz, sz), Image.Resampling.LANCZOS)
        resized.save(os.path.join(out_dir, filename), "PNG")
        print(f"Saved {filename} ({sz}x{sz})")

    # Also save for WebApp
    web_dir = r"C:\Users\vasil\OneDrive\Рабочий стол\gemini lite\WebApp"
    os.makedirs(web_dir, exist_ok=True)
    base_1024.resize((512, 512), Image.Resampling.LANCZOS).save(os.path.join(web_dir, "icon-512.png"), "PNG")
    base_1024.resize((192, 192), Image.Resampling.LANCZOS).save(os.path.join(web_dir, "icon-192.png"), "PNG")
    base_1024.resize((180, 180), Image.Resampling.LANCZOS).save(os.path.join(web_dir, "apple-touch-icon.png"), "PNG")
    print("Saved WebApp icons")

if __name__ == "__main__":
    main()
