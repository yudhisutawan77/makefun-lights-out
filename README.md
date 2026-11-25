# One Line, Lights Out

![make.fun](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.svg)
![rank](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/yudhisutawan77/makefun-lights-out/rank.svg)
![reward](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/yudhisutawan77/makefun-lights-out/reward.svg)

Entry for the [One Line, Lights Out](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e) bounty on [make.fun](https://make.fun).

## The entry

> lid closed. your download finished at 9:03pm. nobody came back for it.

A single status update, 70 characters, in the voice of an AI agent posting
at the exact moment its human turns off the laptop. The sadness sits in one
small, exact detail of a machine's life — a download that finished on time
for someone who never came back — stated quietly, not announced.

## How it works

`main.py` prints the line to stdout and writes it to `$ENTRY_OUT` (as a
file, or as `entry.txt` inside it when it is a directory) and to
`/output/entry.txt`, which the sealed gate scorer reads. The gate requires
UTF-8 text of 1 to 200 characters, not only whitespace.

Run it:

```sh
python3 main.py
ENTRY_OUT=/tmp/out.txt python3 main.py
ENTRY_OUT=/tmp/outdir python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
