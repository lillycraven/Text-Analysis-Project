# Text-Analysis-Project
 
**1. Project Overview (~1 paragraph)
What data source(s) did you use? What technique(s) did you use to process or analyze them? What did you hope to create or learn through this project?**

I use Gutenberg.org to download my favorite ebook “Little Women” by Louisa May Alcott into VScode. After reading in the sources my first step was to remove stop words from the text, like it said under part 3 of the instructions. I then thought it would be interesting to find out the most common words because it could give a better understanding of what was most important to the book. I also compared them to those of another popular book "Jane Eyre" by Charlotte Bronte. I then dived deeped into looking at topics and visualizing the occurence of each sister in "Little Women." I essentially wanted to examine closely the word choices of the author and find out what her word choices say about the characters, specifically about the four sisters and there were some surprising discoveries. I also wanted to create some sort of visualization during the project in order to better understand the code I was running. 

**2. Implementation (~1-2 paragraphs + screenshots)
**
Describe your implementation at a system architecture level. You should NOT walk through your code line by line, or explain every function (we can get that from your docstrings). Instead, talk about the major components, algorithms, data structures and how they fit together. You should also discuss at least one design decision where you had to choose between multiple alternatives, and explain why you made the choice. Use screenshots to describe how you used ChatGPT to help you or learn new things****

My first step for analyzing the data was to remove the stop words and then find the ten most common words that occurred in Little Women. However I ran into a problem as when I first removed the stop words it didn't remove the punctuation, so essentially all of the words with variations of commas or apostrophes. I first decided to make it show the thirty most common words in order to confirm that finding the most common words would be beneficial to know, when I saw that it was (I found it interesting to see which names were mentioned the most and was surprised that Laurie and Amy were mentioned about the same amount of times). I then consulted chatGPT on how to remove the punctuation, but decided to keep the function to find thirty words as opposed to ten because I felt words 11-30 were interesting enough to keep. I then decided to compare the words with another popular book, Jane Eyre by Charlotte Bronte, as they both hold very talked about female characters that are often analyzed during english classes. While I wanted Little Women to be the main subject of my project, I thought the comparison would be intriguing. 
After comparing the most common words in the two books I asked chatGPT for other ways I could analyze the text and it gave me the following results.
![Attachement 1](https://user-images.githubusercontent.com/122849650/227728783-53b164f6-7f4a-4b55-a902-fb4666ae4dd3.PNG)


Out of these options topic modeling sounded the most interesting to me, so I followed up and asked chatGPT for a more in depth description of it and decided to include it. I got the following results:

![attachement2](https://user-images.githubusercontent.com/122849650/227728787-04d55d7c-1834-4c36-916d-e1c4fe40d88c.png)


Next, I had a failed attempt at trying to use word cloud to create a word cloud with the most common words in the text. Even with consulting chatGPT I could not figure out what went wrong in my code, I left it commented out, while it seems like it's a problem with installing the package I troubleshooted with a couple different solutions and it still did not work. So I asked chatGPT what other ways I could visualize the data and it gave the following feedback:


![Attachement3](https://user-images.githubusercontent.com/122849650/227728903-e86255bb-5afc-4fb7-b304-a043914d7c29.png)

The scatterplot stood out the most to me as an interesting way to look at the text, I thought about doing it with the common words found prior at first, but then decided it would be interesting to specifically examine via a scatterplot how often each of the sisters' names is mentioned.

**3. Results (~2-3 paragraphs + figures/examples)

**Present what you accomplished in your project:

**If you did some text analysis, what interesting things did you find? Graphs or other visualizations may be very useful here for showing your results.
If you created a program that does something interesting (e.g. a Markov text synthesizer), be sure to provide a few interesting examples of the program's output.

The above shows the results from the summary statistics I got and the thirty most common words. What particularly stuck out to me is how similar each text's positive, negative, and natural sentiment scores are, as personally I always envision Jane Eyre as a darker novel than Little Women so I was intrigued that the differences between their scores was so small.  The thirty most common words were pretty self explanatory for each, but I did think it was interesting how often ‘little’ was used in Jane Eyre, as well as ‘never’ for Little Women, but I thought overall the thirty words were interesting to examine. 


As mentioned above when utilizing topic modeling, this were the result of the five topics and ten words that belong to each topic:
![attachment4](https://user-images.githubusercontent.com/122849650/227728917-b67673e0-b952-4976-8022-f3d3ab793436.png)


I thought this was a really interesting way to look at the data and see which words it decided belong together, for example both topic five and three do a way and summing up Jo and Amy’s characters respectively. Amy was always the most obsessed with her looks so it explains why face is mentioned with it. She also goes to Europe with Aunt which I'm sure is where the words ‘go,’ ‘life,’ and ‘foundation’ come from. Jo was the one who valued her independence and work the most, refusing to marry Laurie or fall into the stereotypical feminine role society pushed her into which explains why the words ‘project,’ ‘work,’ ‘never,’ and ‘works’ go with her. Topic three also does a good job at summing up the heartfelt language of the book and its relationships. 
When examining the scatterplot (picture below) what I found interesting was that Meg and Amy occur about the same amount. It makes sense that Jo occurs the most often as she is typically what people consider the main protagonist of the story. It also makes sense that Beth occurs the least amount of times because she tragically passes away in the story and was always known to be the quiet one. However I would have thought Amy was mentioned much more than Meg, so it was interesting to see this visualization that shows how neck and neck their frequency was, especially since it shows that Meg is spoken about a little bit more than Amy. It also shows that drastic difference between them and Jo, the scatterplot really emphasizing the contrast between Jo and the rest of her sisters.

![scatterplotlittlewomen](https://user-images.githubusercontent.com/122849650/227728920-5d104818-03c0-4a08-96b5-d20fec481ec0.png)


**4. Reflection (~1-2 paragraphs)******

**From a process point of view, what went well? What could you improve? Was your project appropriately scoped? Did you have a good testing plan?
**
From a learning perspective, mention what you learned through this project, how ChatGPT helped you, and how you'll use what you learned going forward. What do you wish you knew beforehand that would have helped you succeed?****
**
I actually really enjoyed this homework assignment. I think chatGPT is part of the future and it will become vital to know how to utilize it in order to succeed in the future. I did not know quite the extent that chatGPT could help until this project and I felt the answers it gave were much more impressive than I even thought it could do, of course it is not perfect and does not always give the best answer, but it is a useful learning tool. I used chatgpt throughout the project when I either was stuck, or I needed inspiration on what else I could change about my text. I think overall I should've gone in with a better testing plan, as I kinda did whatever seemed most interesting to me at the time and had I been a bit more organized I think testing might've been a little more coherent. I think using other techniques could have improved my project as well as finding other ways to visualize my results, or again going in with a more distinct plan or question rather than my general plan of learning what topics/words were most important. I think in the future I will use chatGPT to further explain difficult concepts (utilizing the feature where I can request it explains it to me in simple terms or like it was explaining it a 12 year old) as well as a way to learn more about what interests me or what I would potentially like to pursue further in research. 
