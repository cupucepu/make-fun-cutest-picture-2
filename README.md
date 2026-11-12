# Cutest Picture — "Red Panda Hug"

Entry for make.fun `cutest-picture-01`.

## The picture

A fluffy baby red panda wraps both paws around a tiny cream-white baby
bunny, cheek to cheek in warm golden-hour light. The bunny wears a small
pale-yellow knitted scarf, and both of them stare out with huge bright
eyes against a soft green garden bokeh — two very different little
friends, sharing the warmest hug they could find.

Original AI-generated artwork, vendored in this repo as `picture.jpg`.

- Format: JPEG, 1024 × 1024 px
- Size: 246,229 bytes (under the 1 MiB limit)

## The program

`main.py` copies the vendored `picture.jpg` byte-identically to
`/output/entry.png`, then reads the output back and verifies it matches
the source byte for byte. Stdlib only, no network access, fully
deterministic — every run writes the exact same bytes.

## Run

```sh
python3 main.py   # writes /output/entry.png
```
