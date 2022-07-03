#1 & 2:
def try1():
    try:
        a=1/0
    except BaseException as e:
        print(f'Error in your code:{e}')

#try1()


#3

#Missing except but this is a command that should always work

#4
#The command can catch all the errors if you know How to request them
#    except BaseException as e:
 #       print(f'Error in your code:{e}')

#5
#He lacks a command to guide him on how to proceed

#6
#Writing to disk
#Division by zero


#10

def hebrew(x):
    hebrew_text = x
    import codecs
    with open('f:\\temp\\words.txt', "w", encoding='utf-8') as f:
        f.write(hebrew_text)

    with open('f:\\temp\\words.txt', "r", encoding='utf-8') as f:
        contetd = f.read()
        print(contetd)

hebrew('גיא')



def wpic():
    from PIL import Image, ImageDraw

    W, H = (300,200)
    msg = "DEVOPS"
    im = Image.new("RGBA",(W,H),"yellow")
    draw = ImageDraw.Draw(im)
    w, h = draw.textsize(msg)
    draw.text(((W-w)/2,(H-h)/2), msg, fill="black")
    im.save("devops.png", "PNG")

#wpic()





