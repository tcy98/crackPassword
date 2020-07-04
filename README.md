# crackPassword

CS3339 Lab3
In this lab we will be cracking passwords. You will be given a list of password hashes and you
must determine the corresponding plain text password for each hash.<br> All of the hashes in this
lab were hashed using SHA256.


Types of passwords to look for<br>
* English words (with both lowercase and uppercase letters)
  * Eggplant, waterfall, kAngaRoO
* 2 words (no spaces, some words may be capitalized)
  * computerScreen, FootballHead, bluecactus
* Common passwords
* Random strings (up to 6 characters)
* Long english words (11 - 26 characters)
* English words with trailing numbers and symbols (up to 4)
  * nerd123!
* English words with letters replaced
  * 1337 h@ck0r
