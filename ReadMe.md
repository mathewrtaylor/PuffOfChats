# PuffOfChats
A function to allow for easy shaped wordcloud creation

## Installation
Clone to the directory of choice, then Pip install the requirements.txt

## Usage Example
```bash
wordpic(Feeds=['http://rss.cbc.ca/lineup/topstories.xml'],
        StopWords=["a", "eh", "sorry"],
        InputImage='CDN_Flag.png',
        OutputImage='words.png')
```

## Credits
Original idea by Craig Helstowski with Finxter - https://blog.finxter.com/how-to-generate-a-word-cloud-with-newspaper3k-and-python/

## License
[MIT](https://choosealicense.com/licenses/mit/)
