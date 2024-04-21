### Decentralized Fantasy Sports Application
- The Application uses a blockchain to securely perform transactions amongst users on the platform. HMAC has been implemented to verify transactions before a miner adds them to the blockchain.
- A matcher adds the possible matches that a user can bet on. On betting the user's transaction request is added to the transaction pool along with its HMAC hash. The miner then verifies the HMAC and validates the transaction before adding it to a block.
- The miner then executes the POW protocol to mine the block and adds it to the blockchain.
- Once the match is ended by the matcher.py, bets can no longer be placed and the funds pooled are redistributed to the users who bet on the winning team in proportion to the amount they bet.

### Steps to run code
- First run `server.py`, this will initialize the blockchain with a genesis block.
- Second run `matcher.py`, you can add one match to the match pool following the instructions. If you press 'Enter', the match will terminate and money will be redistributed. Run multiple such matcher.py codes on different terminals to add multiple active matches. Redistribution of money takes place based on the ratio of people who bet for either team.
- Third run `runner.py`, you can create one user and bet on any of the matches in the match pool, you can view your balance as well.
- Fourth run `miner.py`, you can mine all the current, unmined transactions and get a reward, you can view your balance as well.
- Finally, exit from all the files and press 'Enter' in `server.py` to terminate the application.

### Points to note
- A miner cannot be a betting user. In our implementation, this implies that a miner user and a betting user cannot share the same username.
- Ensure that all the bets on a particular match have been mined before the match ends. 

### Dependencies needed (pip install, unless stated otherwise)
- hmac
- hashlib
- secrets
- json

### Team Members
2021A7PS0467H: Aashish Chandra K 

2021A7PS0234H: Tarimala Vignesh Reddy

2021A7PS0181H: Amit Ghosh

2021A7PS0047H: Tanish Gottimukkala

2021A7PS0430H: Aayush Kumar Singh
