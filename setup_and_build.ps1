# Helper script for Gemini Lite
Write-Host "======================================================" -ForegroundColor Cyan
Write-Host "✨ Gemini Lite for iOS 15.8.7 (iPhone 7 Plus)" -ForegroundColor Cyan
Write-Host "======================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Выберите действие:" -ForegroundColor Yellow
Write-Host "1. Подготовить и отправить проект на GitHub для сборки .IPA в облаке" -ForegroundColor Green
Write-Host "2. Запустить локальный сервер для мгновенного открытия на iPhone (Web-версия)" -ForegroundColor Green
Write-Host "3. Выход" -ForegroundColor Gray
Write-Host ""

$choice = Read-Host "Введите номер (1-3)"

if ($choice -eq "1") {
    Write-Host ""
    Write-Host "1. Создайте новый репозиторий на https://github.com/new" -ForegroundColor Yellow
    Write-Host "2. Скопируйте ссылку на репозиторий (например, https://github.com/surgutovi4/gemini-lite-ios.git)" -ForegroundColor Yellow
    Write-Host ""
    $repoUrl = Read-Host "Вставьте ссылку на ваш GitHub репозиторий"

    if ($repoUrl -ne "") {
        git branch -M main
        git remote remove origin -ErrorAction SilentlyContinue
        git remote add origin $repoUrl
        Write-Host "Отправка в репозиторий $repoUrl..." -ForegroundColor Cyan
        git push -u origin main
        Write-Host ""
        Write-Host "✓ Успешно отправлено! Перейдите во вкладку 'Actions' на GitHub, дождитесь сборки (2 мин) и скачайте GeminiLite.ipa" -ForegroundColor Green
    } else {
        Write-Host "Ссылка не была введена." -ForegroundColor Red
    }
} elseif ($choice -eq "2") {
    # Get local IPv4
    $localIp = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.InterfaceAlias -notmatch "Loopback|vEthernet|Virtual" -and $_.IPAddress -match "^\d+\.\d+\.\d+\.\d+$" } | Select-Object -First 1).IPAddress
    Write-Host ""
    Write-Host "======================================================" -ForegroundColor Cyan
    Write-Host "Локальный сервер запущен!" -ForegroundColor Green
    Write-Host "Откройте Safari на вашем iPhone 7 Plus (подключенном к тому же Wi-Fi) и перейдите по адресу:" -ForegroundColor Yellow
    Write-Host "👉 http://${localIp}:8080/WebApp/" -ForegroundColor Magenta
    Write-Host ""
    Write-Host "В Safari нажмите кнопку 'Поделиться' -> 'На экран Домой'" -ForegroundColor Cyan
    Write-Host "Для остановки сервера нажмите Ctrl + C" -ForegroundColor Gray
    Write-Host "======================================================" -ForegroundColor Cyan
    Write-Host ""
    
    python -m http.server 8080
} else {
    Write-Host "Завершение работы." -ForegroundColor Gray
}
