# AI Desktop Voice Assistant

AI Desktop Voice Assistant is a project built using Microsoft's Speech API, SAPI5 with Python as a backend language.

<h3>Ojective of the project</h3>

The program named 'Jarvis' inspired from the movie "Iron Man" is made for personal use to minimise the effort of opening a website, searching about a famous person or topic on Wikipedia and to know the time and date, without the help of mouse clicks and keyboard.

The further goal is to add plenty other functions to this project to make it versatile. 

<h3>The working of the project</h3>

- Jarvis searches for keywords in the user's audio and based on the keywords found, Jarvis opens those websites for the user. The speech API first converts the user's speech into text. Now, specific keywords are searched for in that text and if found, those websites are opened with the help of WebBrowser library.

- Jarvis can read a couple of lines about a person by searching that person in Wikipedia, if asked for. 

- Jarvis very politely wishes good morning/afternoon/evening based on the time at that moment, and also speaks out the date if asked for.
