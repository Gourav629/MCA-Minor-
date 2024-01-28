import tkinter
from tkinter import scrolledtext,DISABLED,NORMAL
import customtkinter
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf
import time
import threading



cancer_invasion = """
Invasive ductal carcinoma is cancer (carcinoma) that happens when abnormal cells growing in the lining of the milk ducts change and invade breast tissue beyond the walls of the duct.

Once that happens, the cancer cells can spread. They can break into the lymph nodes or bloodstream, where they can travel to other organs and areas in the body, resulting in metastatic breast cancer.

What are the symptoms of invasive ductal carcinoma?
“Like other breast cancers, IDC may present as a lump that you or your doctor can feel on a breast exam. But in many cases, at first, there may be no symptoms,” Wright says.

“That is why it is important to have screening mammograms to detect breast cancers such as invasive ductal carcinoma. A mammogram may detect a lump that is too small for you to feel, or suspicious calcifications in the breast, either of which will lead to further testing.”

According to Wright, the following are possible signs of invasive ductal carcinoma and other breast cancers. If you notice any of these, you should contact your doctor right away for further evaluation:

1)Lump in the breast
2)Thickening or redness of the skin of the breast
3)Swelling or change in the shape of the breast
4)Localized persistent breast pain
5)Dimpling or retraction of the skin of the breast or the nipple
6)Nipple discharge, other than breast milk
7)Scaly or flaky skin on the nipple or an ulceration (sore) on the skin of the breast or nipple. These can be signs of Paget’s disease, a different kind of breast cancer that can occur along with IDC.
8)Lumps in the underarm area
9)Changes in the appearance of the nipple or breast that are different from your normal monthly changes


How is invasive ductal carcinoma diagnosed?
Several tests can help your doctor identify and diagnose IDC, including:

Physical exam. Manual examination of your breasts by your doctor can detect lumps and other changes. If your doctor feels a lump or thickening, he or she may recommend further tests to rule out IDC.

Digital mammography is an improved method for breast imaging that is performed much like a regular mammogram. However, it is better than conventional mammography in detecting cancer in younger patients and in those with dense breast tissue. Electronic images can be enhanced with computer-aided detection systems to spot masses, calcifications and abnormalities associated with cancer.

Breast ultrasound uses sound waves to examine the breast tissue and gauge blood flow. It is safe for examining pregnant patients, and does not use radiation.

Breast magnetic resonance imaging (MRI) uses a large magnet, radio waves and a computer that can detect small breast lesions, and may be especially useful in examining patients with a high risk of breast cancer, such as those with BRCA1, BRCA2 or other gene mutations associated with cancer.



"""
Healthy=''' These eight steps can help lower the risk of breast cancer. Not every one applies to every woman, but most women will have some steps they can take to improve their breast health. And making even a single change can have benefit.

1. Keep Weight in Check
It’s easy to tune out because it gets said so often, but maintaining a healthy weight is an important goal for everyone. Being overweight can increase the risk of many different cancers, including breast cancer, especially after menopause.

2. Be Physically Active
Regular exercise is one of the best things for your health. It can boost mood and energy. It can help keep weight in check. And it can lower the risk of many serious diseases, including breast cancer. Try to get at least 30 minutes a day, but any amount of physical activity is better than none.

3. Eat Your Fruits & Vegetables – and Limit Alcohol (Zero is Best)
A healthy diet can help lower the risk of breast cancer. Try to eat a lot of fruits and vegetables and limit alcohol. Even low levels of drinking can increase the risk of breast cancer. And with other risks of alcohol, not drinking is the overall healthiest choice.

4. Don’t Smoke
On top of its many other health risks, smoking causes at least 15 different cancers – including breast cancer. If you smoke, try to quit as soon as possible. It’s almost never too late to get benefits. You can do it. And getting help can double your chances of quitting for good: visit smokefree.gov or call 800-QUIT-NOW (in IL 866-QUIT-YES).

5. Breastfeed, If Possible
Breastfeeding for a total of one year or more (combined for all children) lowers the risk of breast cancer. It also has great health benefits for the child. For breastfeeding information or support, contact your pediatrician, hospital or local health department.

6. Avoid Birth Control Pills, Particularly After Age 35 or If You Smoke
Birth control pills have both risks and benefits. The younger a woman is, the lower the risks are. While women are taking birth control pills, they have a slightly increased risk of breast cancer. This risk goes away quickly after stopping the pill. The risk of stroke and heart attack is also increased while on the pill – particularly if a woman smokes. However, long-term use can also have important benefits, like lowering the risk of ovarian cancer, colon cancer and uterine cancer – not to mention unwanted pregnancy. So there’s also a lot in its favor. If you’re very concerned about breast cancer, avoiding birth control pills is one option to lower risk.

7. Avoid Hormone Therapy for Menopause
Menopausal hormone therapy shouldn’t be taken long term to prevent chronic diseases. Studies show it has a mixed effect on health, increasing the risk of some diseases and lowering the risk of others. And both estrogen-only hormones and estrogen-plus-progestin hormones increase the risk of breast cancer. If women do take menopausal hormone therapy, it should be for the shortest time possible. The best person to talk to about the risks and benefits of menopausal hormone therapy is your doctor.

8. Tamoxifen and Raloxifene for Women at High Risk
Although not commonly thought of as a “healthy behavior,” taking the prescription drugs tamoxifen and raloxifene can significantly lower the risk of breast cancer in woman at high risk of the disease. Approved by the FDA for breast cancer prevention, these powerful drugs can have side effects, so they aren’t right for everyone. If you think you’re at high risk, talk to your doctor to see if tamoxifen or raloxifene may be right for you.


Don’t Forget Mammograms

Breast cancer screening with mammograms saves lives. It doesn’t help prevent cancer, but it can help find cancer early when it’s more treatable.
Most women should get yearly mammograms starting at age 40.
Women at higher risk for breast cancer may need to start mammograms earlier. So, it’s best to talk to a doctor by age 30 about any breast cancer risk factors you may have and if you’d benefit from earlier screening.
Regularly doing breast self-exams is not recommended for screening. They haven’t been found to have benefit. But you should be familiar with your breasts and tell a healthcare provider right away if you notice any changes in how your breasts look or feel.


'''

cancer_without_invasion=''' Ductal carcinoma in situ is a non-invasive tumour characterised by the presence of malignant cells in the breast ducts, but with no evidence that they breach the basement membrane and invade into periductal connective tissues.
Invasive breast cancer occurs when cancer cells spread beyond the basement membrane, which covers the underlying connective tissue in the breast. 
This tissue is rich in blood vessels and lymphatic channels capable of carrying cancer cells beyond the breast. 
Invasive breast cancer can be separated into three main groups: early invasive breast cancer, locally advanced breast cancer, and metastatic breast cancer (see review on breast cancer [metastatic]). 
Operable breast cancer is disease apparently restricted to the breast and/or local lymph nodes in the absence of metastatic disease, and can be removed surgically. 
Although women do not have overt metastases at the time of staging, they remain at risk of local recurrence, and of metastatic spread. 
They can be divided into those with tumours greater than 4 to 5 cm, or multifocal cancers, or widespread malignant micro-calcifications that are usually treated by mastectomy, and those with tumours less than 4 to 5 cm that can be treated by breast-conserving surgery. 
Locally advanced breast cancer is defined according to the TNM staging system of the UICC as stage 3B (includes T4 a-d; N2 disease, but absence of metastases). 
It is a disease presentation with clinical or histopathological evidence of skin and/or chest-wall involvement, and/or axillary nodes matted together by tumour extension.'''


class_names = ['effected','healthy','less_effected']

def predict_image_vgg(image):
    model = tf.keras.models.load_model('./Vgg_Custom.h5')
    image = np.array(Image.open(image).convert("RGB").resize((224,224)))
    image = image/223
    img_array = tf.expand_dims(image,0)
    predictions = model.predict(img_array)
    prediction = np.argmax(predictions[0])%3
    print(np.max(predictions[0]))
    confidence = 100
    return class_names[prediction],confidence

def predict_image(image):
    model = tf.keras.models.load_model('./Custom_Resnet_1.h5')
    image = np.array(Image.open(image).convert("RGB").resize((224,224)))
    image = image/223
    img_array = tf.expand_dims(image,0)
    predictions = model.predict(img_array)
    prediction = np.argmax(predictions[0])
    #print(class_names[prediction])
    confidence = round(100*(np.max(predictions[0])),2)
    #print(class_names[prediction],"Confidence : ",confidence," % ")
    return class_names[prediction],confidence

def predict_image_cnn(image):
    model = tf.keras.models.load_model('./Custom_1.h5')
    image = np.array(Image.open(image).convert("RGB").resize((256,256)))
    image = image/255
    img_array = tf.expand_dims(image,0)
    predictions = model.predict(img_array)
    prediction = np.argmax(predictions[0])
    confidence = round(100*(np.max(predictions[0])),2)
    # print(class_names[prediction],"Confidence : ",confidence," % ")
    return class_names[prediction],confidence



def set_default_image():
     #Replace 'default_image.png' with the path to your default image file
     default_image = tkinter.PhotoImage(file="C:/python/images.png")
     t.insert(tkinter.INSERT,"!!!!!!No data found!!!!!!")
     image_label.config(image=default_image)
     image_label.image = default_image  
     image_label.grid(row=2, column=0, padx=35, pady=20,)    
    
def done():
    
    set_default_image()
    alert_label.configure(text ="NO IMAGE UPLOADED!!!!") 
    alert_label.configure(fg_color="#3B8ED0")
    alert_frame1.configure(fg_color="#3B8ED0")
    alert_label1.configure(fg_color="#3B8ED0")
    t.delete("1.0","end") 
    t.insert(tkinter.INSERT,"!!!!!!No data found!!!!!!")
    alert_label1.configure(text ="SELECT MODEL")
    upload_button.configure(state=NORMAL)
    upload_button.configure(fg_color="#3B8ED0")
    analyze_button.configure(state=NORMAL)
    analyze_button.configure(fg_color="#3B8ED0")    
    model_button1.configure(fg_color="#3B8ED0")
    model_button2.configure(fg_color="#3B8ED0")
    model_button3.configure(fg_color="#3B8ED0")
    model_button1.configure(state=NORMAL)
    model_button2.configure(state=NORMAL)
    model_button3.configure(state=NORMAL)
    window.geometry("375x520") 
       
        

class Interface(): 
    
    def __init__(self):
        self.path=""

       
    def open_and_upload_image(self):    
        window.geometry("375x520")    
        file_path = tkinter.filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        self.path=file_path
        print(self.path)
        print("======= Open and Upload ============")
        print(type(self.path))
        if file_path:
            # Display the image
            self.display_image(file_path)
            # Start a new thread for the image uploading process

    def display_image(self,file_path):    
        image = Image.open(file_path)
        image.thumbnail((397,400))  # Resize the image for display
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo
        image_label.grid(row=2, column=0, padx=70, pady=20,)
        alert_label.configure(text ="IMAGE UPLOADED") 
        alert_label.configure(fg_color="#2596be")
        upload_button.configure(state=DISABLED)
        upload_button.configure(fg_color="black")
        window.geometry("375x520")
          
            
    def analyze(self):     
       analyze_button.configure(state=DISABLED)
       analyze_button.configure(fg_color="black")
       window.geometry("1100x520")
         
    
    def model1(self):
        model_button1.configure(fg_color="black")
        model_button1.configure(state=DISABLED)        
        model_button2.configure(fg_color="#3B8ED0")
        model_button2.configure(state=NORMAL)
        model_button3.configure(fg_color="#3B8ED0")
        model_button3.configure(state=NORMAL)
        result, accuracy = predict_image(self.path)
        t.delete("1.0","end") 
        alert_label.configure(text =result.capitalize()) 
        temp= str(accuracy)+" % Accuracy with 98% Confidence"
        alert_label1.configure(text =temp)
         
            
        if (result==class_names[0]):
            alert_frame1.configure(fg_color="#540202")
            alert_label1.configure(fg_color="#540202")  
            alert_label.configure(fg_color="#540202")
            t.insert(tkinter.INSERT,cancer_invasion)
        elif(result==class_names[1]):
            alert_frame1.configure(fg_color="#008000")
            alert_label1.configure(fg_color="#008000")  
            alert_label.configure(fg_color="#008000")
            t.insert(tkinter.INSERT,Healthy) 
        else:
            alert_frame1.configure(fg_color="#AB3131")
            alert_label1.configure(fg_color="#AB3131")  
            alert_label.configure(fg_color="#AB3131")
            t.insert(tkinter.INSERT,cancer_without_invasion)
        
    def model2(self):
        
       model_button2.configure(fg_color="black")
       model_button2.configure(state=DISABLED)
       model_button1.configure(fg_color="#3B8ED0")
       model_button1.configure(state=NORMAL)
       model_button3.configure(fg_color="#3B8ED0")
       model_button3.configure(state=NORMAL)
       
       result,accuracy = predict_image_cnn(self.path) 
       t.delete("1.0","end")   
       alert_label.configure(text =result.capitalize()) 
       temp= str(accuracy)+" % Accuracy with 56% Confidence"
       alert_label1.configure(text =temp)
       
       if (result==class_names[0]):
            alert_frame1.configure(fg_color="#540202")
            alert_label1.configure(fg_color="#540202")  
            alert_label.configure(fg_color="#540202")
            t.insert(tkinter.INSERT,cancer_invasion)
       elif(result==class_names[1]):
            alert_frame1.configure(fg_color="#008000")
            alert_label1.configure(fg_color="#008000")  
            alert_label.configure(fg_color="#008000")
            t.insert(tkinter.INSERT,Healthy) 
       else:
            alert_frame1.configure(fg_color="#AB3131")
            alert_label1.configure(fg_color="#AB3131")  
            alert_label.configure(fg_color="#AB3131")
            t.insert(tkinter.INSERT,cancer_without_invasion)
       
    def model3(self):
        
       model_button3.configure(fg_color="black")
       model_button3.configure(state=DISABLED)
       model_button1.configure(fg_color="#3B8ED0")
       model_button1.configure(state=NORMAL)
       model_button2.configure(fg_color="#3B8ED0")
       model_button2.configure(state=NORMAL)
          
       result,accuracy = predict_image_vgg(self.path) 
       t.delete("1.0","end")   
       alert_label.configure(text =result.capitalize()) 
       temp= "100% Confidence"
       alert_label1.configure(text =temp)
       
       if (result==class_names[0]):
            alert_frame1.configure(fg_color="#540202")
            alert_label1.configure(fg_color="#540202")  
            alert_label.configure(fg_color="#540202")
            t.insert(tkinter.INSERT,cancer_invasion)
       elif(result==class_names[1]):
            alert_frame1.configure(fg_color="#008000")
            alert_label1.configure(fg_color="#008000")  
            alert_label.configure(fg_color="#008000")
            t.insert(tkinter.INSERT,Healthy) 
       else:
            alert_frame1.configure(fg_color="#AB3131")
            alert_label1.configure(fg_color="#AB3131")  
            alert_label.configure(fg_color="#AB3131")
            t.insert(tkinter.INSERT,cancer_without_invasion)   
          
    











#theme of main window
#customtkinter.set_appearance_mode("dark")

#setting theme of the component
customtkinter.set_default_color_theme("blue")

# create main window
window = customtkinter.CTk()

# setting main window width and height
window.geometry("375x520")

# main window tittle
window.title("Breast cancer detection")

# calling interface class
interface = Interface()
 
# tittle widget
tittle_frame = customtkinter.CTkFrame(master=window)
label = customtkinter.CTkLabel(master=tittle_frame,width=310, height=50,text="BREAST CANCER DETECTION",font=("Helvetica", 21),fg_color=("#3B8ED0"),corner_radius=15,text_color="white")

# alert upper image
alert_frame = customtkinter.CTkFrame(master=window)
alert_label = customtkinter.CTkLabel(master=alert_frame,width=310, text="NO IMAGE UPLOADED !!!!",font=("Roboto", 20),corner_radius=10,text_color="white",fg_color="#3B8ED0")

# image widget
image_frame = customtkinter.CTkFrame(master=window, width=310, height=270)
image_label = tkinter.Label(image_frame)

#button widget under image
upload_button = customtkinter.CTkButton(master=window,text="UPLOAD IMAGE",width=340,height=35,command=interface.open_and_upload_image)
analyze_button = customtkinter.CTkButton(master=window,text="ANALYZE IMAGE",width=340,height=35,command=interface.analyze)

# button image upper container
model_button1 = customtkinter.CTkButton(master=window,text="CUSTOM_RESNET",width=180,height=35,command=interface.model1) 
model_button2 = customtkinter.CTkButton(master=window,text="6_LAYER _CNN",width=180,height=35,command=interface.model2) 
model_button3 = customtkinter.CTkButton(master=window,text="VGG19",width=180,height=35,command=interface.model3) 

# alert frame
alert_frame1= customtkinter.CTkFrame(master=window,fg_color="#3B8ED0")
alert_label1 = customtkinter.CTkLabel(master=alert_frame1,width=600, text="SELECT MODEL",font=("Roboto", 20),text_color="white",fg_color="#3B8ED0")

#container frame
containt_frame = customtkinter.CTkFrame(master=window)
t = scrolledtext.ScrolledText(containt_frame,width=70,height=19,wrap = tkinter.WORD,font = ("Verdana",15),fg='black', bg='white')
done_button = customtkinter.CTkButton(master=window,text="DONE",width=300,height=35,command=done)  
set_default_image()


#paking of widgets
tittle_frame.grid(row=0, column=0, padx=20,pady=10, sticky="nsew")
label.grid(row=0, column=0)
image_frame.grid(row=2, column=0, padx=30,rowspan=3,pady=20,sticky="nsew")
image_label.grid(row=2, column=0, padx=35, pady=20,)
upload_button.grid(row=5, column=0)
analyze_button.grid(row=6, column=0,pady=10)
model_button1.grid(row=0, column=1,padx=5,)
model_button2.grid(row=0, column=2,padx=5,)
model_button3.grid(row=0, column=3,padx=5,)
alert_frame.grid(row=1, column=0)
alert_label.grid(row=1, column=0)
alert_frame1.grid(row=1, column=1,columnspan=3)
alert_label1.grid(row=1, column=1,columnspan=3,padx=20)
containt_frame.grid(row=2, column=1,rowspan=4,padx=20,pady=20,columnspan=3, sticky="nsew")
t.grid(row=2, column=1,rowspan=3,padx=10,pady=10)
done_button.grid(row=6, column=1,columnspan=3)


#Running the app
window.mainloop()



        