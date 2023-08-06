

from IPython.core.display import display,  HTML
import string
import random
import json
import urllib
import pkg_resources

def display_flashcards(ref):



    resource_package = __name__
    styles = "<style>\n"
    css = pkg_resources.resource_string(resource_package, "styles.css")
    styles += css.decode("utf-8")
    styles += "\n</style>"

    #script ='<script src="swiped-events.min.js"></script>'

    script = '<script type="text/Javascript">\n'
    js = pkg_resources.resource_string(resource_package, "swiped-events.min.js")
    script += js.decode("utf-8")
    js = pkg_resources.resource_string(resource_package, "flashcards.js")
    script += js.decode("utf-8")
    script += "\n</script>"

    #print(script)



    #print(card["front"], card["back"])
    letters = string.ascii_letters
    div_id = ''.join(random.choice(letters) for i in range(12))
    #div_id='ABBA'
    # print(div_id)

    # Container
    #mydiv =  '<div class="flip-container" id="'+ div_id + '"></div>'
    mydiv =  f'<div class="flip-container" id="{div_id}" onclick="flip(this)"></div>'



    #Spacer
    spacer='<div style="height:40px"></div>'

    # Next button will go here
    nextbutton=f"""<div class="next" id="{div_id}-next" onclick="checkFlip('{div_id}')"> </div> """
    
    #print(nextbutton)
    loadData = '''<script type="text/Javascript">
    
    '''

    loadData += "cards"+div_id+"="

    if type(ref) == list:
        #print("List detected. Assuming JSON")
        loadData += json.dumps(ref)
        static = True
        url = ""
    elif type(ref) == str:
        if ref.lower().find("http") == 0:
            url = ref
            file = urllib.request.urlopen(url)
            for line in file:
                loadData += line.decode("utf-8")
            static = False
        else:
            #print("File detected")
            with open(ref) as file:
                for line in file:
                    loadData += line
            static = True
            url = ""
    else:
        raise Exception("First argument must be list (JSON), URL, or file ref")

    loadData += ''';
    '''
    
    if static:
        loadData += f'''
        createCards("{div_id}");
        </script>
        '''

        print()
    else:
        loadData += f'''

        {{
        const jmscontroller = new AbortController();
        const signal = jmscontroller.signal;

        setTimeout(() => jmscontroller.abort(), 5000);

        fetch("{url}", {{signal}})
        .then(response => response.json())
        .then(json => createCards("{div_id}"))
        .catch(err => {{
        console.log("Fetch error or timeout");
        createCards("{div_id}");
        }});
        }}
        </script>
        '''
        #loadData+=url+script_end


    #print(loadData)
    display(HTML(styles+script+loadData+spacer+mydiv+spacer+nextbutton+spacer))
