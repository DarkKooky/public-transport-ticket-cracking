# [Ressources](https://github.com/DarkKooky/public-transport-ticket-cracking/tree/main/resources)
Each file contains data scanned from a non-nominative public transport tickets by my [Flipper](https://flipperzero.one)'s NFC reader.
The file naming goes as follows: `<CARD>_<CRED>.nfc`
- `<CARD>` describes the mark I inscribed onto the ticket to differentiate them
  - `a_8` represents ticket `a`
  - `b_0` represents ticket `b`
  - `b_1` represents ticket `b`

- `<CRED>` describes the amount of credits held by the ticket
  - `a_8` holds `8` credits
  - `b_0` holds `0` credit
  - `b_1` holds `1` credit
# Current State
By comparing [b_0.nfc]() and [b_1.nfc](), I can only suppose that the data pertaining to the credits is stored in blocks range `[5, 6]` and `[11, 14]`, as the program only found differences in those blocks.