import xml.dom.minidom as prettifier

def convert(filename):
    dom = prettifier.parse(filename)
    preetified_string = dom.toprettyxml()
    splitting_text = preetified_string.replace('\t'," ").split("\n")[2:-1]
    output = ""
    
    for i in splitting_text:
        if len(i)!=0 and (i !=" "):
            if (i[:2]==" <") :
                i=i[1:]
                Type = i[1:i.find(" ")]
                
                enitity = i[i.find(">")+1:i.find("</")]
                output += enitity+"  "+Type+"\n"
            else:
                
                temp_words = i.split(" ")
                for word in temp_words:
                    if len(word)!=0:       
                        output+=word+"  "+"O\n"
                    
        else :
            pass
    with open('stanford_output.txt','a') as f:
        f.write(output+"\n\n")

