Import-Module activedirectory

$username = "Franz Ferdinand"
$password = "SecurePassword"
$firstname = "Franz"
$lastname = "Ferdinand"
$OUPath = "OU=TPS,OU=Departments,DC=GlobeX,DC=com"
$email = "ferdi@GlobeXpower.com"

New-ADUser -Name $username -GivenName $firstname -Surname $lastname -AccountPassword (ConvertTo-SecureString -AsPlainText $password -Force) -EmailAddress $email -Path $OUPath -Enabled $true

Set-ADUser -Identity $username -Department "TPS" -Office "Springfield, OR" -Title "TPS Reporting Lead"