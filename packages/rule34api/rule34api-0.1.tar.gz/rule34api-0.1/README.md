# Rule34-API

Syncronized Rule34 API Wrapper

## Usage
```python
import rule34

rule34.count_images('gay tentacle hentai')
images = rule34.get_images('gay tentacle hentai', page=0)

print("The Image from {author} has following tags: \'{tags}\'".format(
  author=image.owner,
  tags=image.tags
))
```

> :warning: Indexing start with Page `0`!

## GitHub
This Wrapper is maintained on (GitHub)["https://github.com/hide-and-hentai/rule34-api"]!
We will take a look at every Pull Request.
If you have issues or need help with implementing this Wrapper, create an Issue.
