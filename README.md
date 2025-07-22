# Secure (almost) Poke Api 

## Installation

```bash
uv sync
make migrate
make populate
make dev
```


## Tests


You need to create an test account and adapt login into it.
Tests consider the account "test/test" exists and can login

```bash
hurl hurl/login.hurl --test
hurl hurl/pokemon.hurl --test
```
