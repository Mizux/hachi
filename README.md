# Hachi

A monster-catching jrpg like game but in a cyberpunk world.

## Documentation

- [Hachi Type Chart](docs/hachi.md)
- [Hachi Type Extension Proposals](docs/proposal.md)
- [Pokemon Type Chart](docs/pkm.md)

## Setup

```sh
rustup default stable
rustup target add wasm32-unknown-unknown
```

To bundle you need `trunk`...

```sh
pacman -S trunk
# or
cargo install trunk
export PATH=${PATH}:${HOME}/.cargo/bin/
```

## Build & Test

* Linux Terminal: `cargo run --bin hachi`

* Browser: `trunk serve`
