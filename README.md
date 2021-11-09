# parse-html-to-json
This script will read all the html file in `data` directory and create a json in this format
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
python3 main.py
