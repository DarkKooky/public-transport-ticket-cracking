# [Ressources](https://github.com/DarkKooky/public-transport-ticket-cracking/tree/main/resources)
Each file contains data scanned from a non-nominative public transport tickets by my [Flipper](https://flipperzero.one)'s NFC reader.
The file naming goes as follows: `<CARD>_<CRED>.nfc`
### `<CARD>`
It describes the mark I inscribed onto the ticket to differentiate them.
- `a_8` represents ticket `a`
- `b_0` represents ticket `b`
- `b_1` represents ticket `b`
### `<CRED>`
It describes the amount of credits held by the ticket.
- `a_8` holds `8` credits
- `b_0` holds `0` credit
- `b_1` holds `1` credit
### More About Ticket `b`
On the 30/04/2024, ticket `b` was:
- Bought with `1` credit
- Scanned and data saved as `b_1`
- Used on public transport, bringing the credit down to `0`
- Scanned again and data saved as `b_0`
# Current State
The function `find_ticket_data_differences`, in [data_manipulator.py](https://github.com/DarkKooky/public-transport-ticket-cracking/blob/main/modules/data_manipulator.py), found that between [b_0.nfc](https://github.com/DarkKooky/public-transport-ticket-cracking/blob/main/resources/b_0.nfc) and [b_1.nfc](https://github.com/DarkKooky/public-transport-ticket-cracking/blob/main/resources/b_1.nfc), the differences are found in block ranges `[5, 6]` and `[11, 14]`. As the files represent an identical ticket before and after usage on public transport, I can only assume that the data pertaining to credit counting is stored in those blocks.
