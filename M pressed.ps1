Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Media

$player = New-Object System.Media.SoundPlayer
$player.SoundLocation = "E:\epic games\youtube XL\alt-J - Tessellate [OFFICIAL VIDEO] - alt-J.wav"

Write-Host "Press M to play sound. Press ESC to exit."

while ($true) {
    $key = [System.Windows.Forms.Control]::ModifierKeys
    if ([Console]::KeyAvailable) {
        $pressed = [Console]::ReadKey($true)

        if ($pressed.Key -eq "M") {
            $player.Play()
            Write-Host "M pressed 😭"
        }

        if ($pressed.Key -eq "Escape") {
            break
        }
    }
}