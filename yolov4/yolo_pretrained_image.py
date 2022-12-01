# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 13:48:11 2022
@author: recep

Hazır model yolov3
"""
# %% 1. bölüm
import cv2
import numpy as np

img = cv2.imread("E:/YOLO/yolo pretrained image/images/img2.jpg")

img_width = img.shape[1]  # görselin genişlik değerini değişkene atadık
img_heigth = img.shape[0]  # görselin uzunluk değerini değişkene atadık
# konsola img.shape yazınca çıkan değerler değişkenlere atanmış oldu

# görseli algoritmaya vermek için öncelikle onu blob formata dönüştürmemiz lazım
# bunun için bi fonksiyon kullanağız 5 tane parametre alıyor


# %% 2. bölüm

img_blob = cv2.dnn.blobFromImage(img, 1 / 255, (416, 416), swapRB=True, crop=False)
# p1 -> blob formata dönüştürelecek görselin tutulduğu değişken
# p2-> resmin yeniden boyutlandırılması için bir değer (yolo yazarları bunun-
# en ideal oranın 1/255 olduğunu belirtiyor)
# p3-> blobun kaça kaçlık olası gerektiğii belirtiyoruz bizim kullandığımız-
# veri seti 416x416
# göreslin formatını BGR den RGB ye çevirmemiz lazım (cv2.imread fonksiyonu BGR-
# olarak okur)
# p5-> nesneyi kırmak istediğimizde kullanırız kullanmayacağız için False yaptık
# en son terminale img_blob.shape yazarsak oluşturulan tensorun (1, 3, 416, 416)-
# olan 4 boyutlu bir matris olduğu görülür

# kaç tane tanıyacağımız nesne varsa onları labelda ismilerini girdik

labels = ["person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat",
          "trafficlight", "firehydrant", "stopsign", "parkingmeter", "bench", "bird", "cat",
          "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack",
          "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sportsball",
          "kite", "baseballbat", "baseballglove", "skateboard", "surfboard", "tennisracket",
          "bottle", "wineglass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
          "sandwich", "orange", "broccoli", "carrot", "hotdog", "pizza", "donut", "cake", "chair",
          "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse",
          "remote", "keyboard", "cellphone", "microwave", "oven", "toaster", "sink", "refrigerator",
          "book", "clock", "vase", "scissors", "teddybear", "hairdrier", "toothbrush"]

# herbir nesne için farklı renkler tanımlamamız lazım
colors = ["0,255,255", "0,0,255", "255,0,0", "255,255,0", "0,255,0"]
# her bir virgülden itibaren ayrıp, renk değerlerini tek tek int tipine çevirmemiz lazım
colors = [np.array(color.split(",")).astype("int") for color in colors]
# değişkenlerin değerlerini int'e çevirdik şimdi bunları tek bir arrayde toplayalım
colors = np.array(colors)
# color arrayinin yeni halinde 5 tane nesneye yetecek çeşitlilikte renk var-
# daha fazla renk türetmek için numpy'ın bi fonksiyonunu kulanırız
colors = np.tile(colors, (18, 1))
# 1.P -> alt atlta kaç kere ekleneceği
# 2.P -> yanyana kaç kere ekelneceği hiç ekleyemeyeceğmiz için 1 yazdık

# Hazır veri setinden aldığımız cfg ve weights doslarının değerini-
# bir değişkene atayalım


# %% 3.bölüm

model = cv2.dnn.readNetFromDarknet("E:/YOLO/pretrained_model/yolov3.cfg", "E:/YOLO/pretrained_model/yolov3.weights")
layers = model.getLayerNames()
# ditection işlemi yapabilmek için modeldeki layerlerı çekmemiz gerekiyor-
# yukardaki satırda bunu yaptık sonuc olarak 254 tane değişkenli bir tuple oldu
# Bize sadece ditection yapılan katmanlar lazım olduğu için onları bir işlemle
# çekmeliyiz(çıktı katmanları) bunları tek tek aramak yerine bir komut kullacağız
# kullandığız bu komut aradığımız değerlerin bir fazlasını verdiği için her
# birinden bir çıkarmalıyız

output_layer = [layers[layer - 1] for layer in model.getUnconnectedOutLayers()]
model.setInput(img_blob)
detection_layers = model.forward(output_layer)
# %% 4.bölüm

# bu kısımda 3.bölümde elde ettiğimiz detection_layers'in içerisini for ile
# gezeceğiz bu değişken 3 tane matrisin oluştuğu bir tuple

for detection_layer in detection_layers:  # 3 listeyi gezdik
    for object_detection in detection_layer:  # listelerin herbirinin içini gezdik
        # object_detection da for ile  elde edeceğimiz ilk 5 değer boundingboxlarla-
        # ilgili bunları ilerde kullacağız şuanlık bi işimiz yok
        # şuan güven skorlarınıyla işimiz var bunlar 5ten sonrai değerlerdir.
        scores = object_detection[5:]
        # bu scores değerleri içinde en büyük değere sahip olanlar ise bizim
        # nesnemize iat toplam skorlar içinde e büyük olnalrı ayırmamız lazım
        predicted_id = np.argmax(scores)
        # bu komut bize en büyük değere sahip elamanın index numarısını döndürür
        confidence = scores[predicted_id]

        if confidence > 0.80:  # güven skoru %30 dan büyükse
            label = labels[predicted_id]
            # tanıdınan nesnenin label'ı ile ilişkilendirmek gerekiyor

            # şimdi boundingbox'ı işlemlerini yapalım
            bounding_box = object_detection[0:4] * np.array([img_width, img_heigth, img_width, img_heigth])
            # boundingbox ile ilgili kısımlar ilk 5 elemandı fakat bunları kullanabilmemiz-
            # için bu değeri ilk başta belirlediğiömiz görselin genişliği ve yükseliği
            # ile çarpmamız lazım
            # tanımlanan nesnenin etrafında bir dörtgen çerçeve çizelim şimdi
            (box_center_x, box_center_y, box_width, box_height) = bounding_box.astype("int")
            # kutu için gerekli olan doktaları çekti ve int'e çevirdik çünkü float değerler
            # ile çizdiremeyiz
            # bu işlemden sonra dörtgenin başlangıc ve bitiş kordinatlarını belirlememiz lazım
            start_x = int(box_center_x - (box_width / 2))
            start_y = int(box_center_y - (box_height / 2))
            # her işlemden sonra int'e çevirmek önemli çünkü dikdörtgen çizdirme komutu
            # int değerlerle çalışıyor
            end_x = start_x + box_width
            end_y = start_y + box_height
            # bundan sonra kutunun rengini ayarlarız
            box_color = colors[predicted_id]
            # predicted_id her nesneiçin ayrı olacağı için her nesneye ayrı bir renk atanmış olacak
            box_color = [int(each) for each in box_color]
            # herbir rengi bir listede tuttuk ve int olduğuna emin olmak için int'e çevirdik

            # şimdi boundinbox'ımızı çizdirelim
            cv2.rectangle(img, (start_x, start_y), (end_x, end_y), box_color, 1)
            # 1.p-> çizim yapacağımız görüntü
            # 2.p-> başlangıç noktanın x ve y değeri
            # 3.p-> bitiş noktasının x ve y değeri
            # 4.p-> renk 5.p-> kalınlık

            # görüntüde çerçevinin kenarında yazdırlacak olan metni ayarlayalım
            cv2.putText(img, label, (start_x, start_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, box_color, 1)

            # labeları terminalleden görebilmek için extra şu komutları yazdık
            label = "{}: {:.2f}%".format(label, confidence * 100)
            # burada bir formatlama yaptık, burada ilk küme parantezine label yazıalcak
            # ikinci küme parantezine confidance*100 değeri yazılacak
            # :.2f ile float değerin ondaliklı kısmın 2 basamağını göstermesini sağlayacak
            print("predicted object {}".format(label))

cv2.imshow("Detection Window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()





























