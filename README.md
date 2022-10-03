# Fake Hacker Terminal
Python script for loosely replicating the 'hacker view' of an 'attack'. 

Useful for user awareness demos or training videos for a non-technial audience.

![Demo](https://user-images.githubusercontent.com/100603074/193573191-57d38872-e0d7-47ab-b55d-fab214eb9059.gif)

**Install:** `git clone https://github.com/A-poc/FakeHackerTerminal;cd FakeHackerTerminal;pip install -r requirements.txt`

**Run:** `python3 AttackDemo.py`

### Attacker Actions (*Change to match desired outputs*):
  - Starts meterpreter listener
  - Catches meterpreter reverse shell
  - Runs getuid (Returns current user)
  - Runs ipconfig (Returns basic network information)
  - Runs killav (Disables EDR/Antivirus on endpoint)
  - Runs getsystem (Leverages named pipe impersonation to elevate privs)
  - Runs hashdump (Returns fake output of credentials for demo)
  - Runs enable_rdp (Enables remote desktop for further visual)
