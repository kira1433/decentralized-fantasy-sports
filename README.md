### Decentralized Fantasy Sports Application
- The Application uses a blockchain to securely perform transactions amongst users on the platform. HMAC has been implemented to verify transactions before a miner adds them to the blockchain.
- A matcher adds the possible matches that a user can bet on. On betting the user's transaction request is added to the transaction pool along with its HMAC hash. The miner then verifies the HMAC and validates the transaction before adding it to a block.
- Once the match is ended by the matcher.py, bets can no longer be placed and the funds pooled are redistributed to the users who bet on the winning team in proportion to the amount they bet.

### Steps to run code
Run server.py, matcher.py, runner.py and miner.py in the respective order and follow the menu instructions.

### Team Members
2021A7PS0467H: Aashish Chandra K 

2021A7PS0234H: Tarimala Vignesh Reddy

2021A7PS0181H: Amit Ghosh

2021A7PS0047H: Tanish Gottimukkala

2021A7PS0430H: Aayush Kumar Singh
