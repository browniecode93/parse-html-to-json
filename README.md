# parse-html-to-json
This script will read all the html file in `data` directory and create a json in this format and save the result on result.json on the same directory.
```
[
  {
    artist: 'Pablo Picasso',
    works: [
      { title: 'Femme accroupie (Jacqueline)', currency: 'GBP', amount: '25,000' },
      ...
    ],
  },
  ...
]
```

# Usage
pip3 install -r requirements.txt
python3 main.py
