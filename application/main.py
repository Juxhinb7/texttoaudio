import pyttsx3
import sys
import trafilatura
import os 




app = pyttsx3.init()
rate = app.getProperty("rate")
app.setProperty("rate", rate-70)
voices = app.getProperty("voices")
app.setProperty("voice", voices[0].id)


try:
    if (str(sys.argv[1]) == "fetch" and str(sys.argv[2]) is not None):
        category_fetched = trafilatura.fetch_url("https://de.wikibooks.org/wiki/Regal:{}".format(sys.argv[2]))
        text = trafilatura.extract(category_fetched)
        print(text)
        user_input = input("Choose one field. Note! Words that contain whitespaces need to be written with an underscore('_'): ")
        url_fetched = trafilatura.fetch_url("https://de.wikibooks.org/wiki/{}".format(user_input))
        url_text = trafilatura.extract(url_fetched, with_metadata=False)
        print(url_text)
        subcategory_input = input("Choose one subcategory. Note! Words that contain whitespaces need to be written with an underscore('_'): ")
        subcategory_fetched = trafilatura.fetch_url("https://de.wikibooks.org/wiki/{}/_{}".format(user_input, subcategory_input))
        sub_fetched_alternative = trafilatura.fetch_url("https://de.wikibooks.org/wiki/{}:_{}".format(user_input, subcategory_input))
        subcategory_text = trafilatura.extract(subcategory_fetched)

        if (subcategory_text is None):
            subcategory_text = trafilatura.extract(sub_fetched_alternative)
            print(subcategory_text)
         
        to_save_or_not_to_save = input("Do you wish to save the text as audio? (y/n):")
        if (to_save_or_not_to_save == "y"):
            if not os.path.exists(sys.argv[2]):
                os.mkdir(sys.argv[2])
            
            audio_format = input("Choose a format(mp3, wav): ")
            if (audio_format == "mp3"):
                app.save_to_file(subcategory_text, "{}/{}.{}".format(sys.argv[2], subcategory_input, audio_format))
            elif(audio_format == "wav"):
                app.save_to_file(subcategory_text, "{}/{}.{}".format(sys.argv[2], subcategory_input, audio_format))
            else:
                raise ValueError        
        
        

except Exception as e:
    print(e)
    
    

app.runAndWait()
