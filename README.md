# Fula-UNMT: Unsupervised Neural Machine Translation for Fula-English

This is an ongoing work on Unsupervised Neural Machine Translation for Fula-English. Neural Machine Translation (NMT) has shown significant success lately, but most of the success is achieved for the world's most popular languages like English and French. Despite making up a large percentage of the world's living languages today, African languages lack good quality text corpora and this hinders machine translation research.

I decided to work on Unsupervised Neural Machine Translation (UNMT) for Fula. Fula is a member of the Senegambian branch of the Niger-Congo language family spoken by about 18 million people across about 20 countries in West and Central Africa. Fula is spoken as a set of various dialects. The language is known by other names: Fulah, Ful, Fulfulde, Fulani, Fulbe, Peul, Pular, and Pulaar.

## Data Gathering
We used Scrapy to crawl a number of websites to get monolingual data for the Fula language. These websites are:
- [Pulaar.org - A multimedia news and advocacy website in Pulaar (Mauritania)](https://pulaar.org/)
- [Binndi Pulaar - A news website on culture, history, language, and politics (Senegal)](https://binndipulaar.com/)
- [Dingiral Fulbe (Senegal)](https://dingiralfulbe.com/)
- [Teddungal Damal Pulaaku (Guinea)](https://teddungal.wordpress.com/)
- [Hammadi-Jah (Science Blog - Mauritania)](https://hammadi-jah.skyrock.com/)
- [Pular New Testament Bible (Guinea)](https://live.bible.is/bible/FUFPBT/)

The code for all the crawlers are in the `crawlers` folder of this project.

Author: Allen Akinkunle ([LinkedIn](https://www.linkedin.com/in/allenkunle/), [Twitter](https://twitter.com/allenakinkunle))
