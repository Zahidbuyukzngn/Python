#Pyplot ile çubuk grafikler çizmek için bar() fonksiyonunu kullanabilirsiniz:

import matplotlib.pyplot as plt
import numpy as np

x=np.array(["A","B","C","D"])
y=np.array([20,50,25,75])

#bar fonk. genişlik için width kullan
plt.bar(x,y,color='cyan',width=0.2)
plt.show()

#dikey yerine yatay cubuklar
import matplotlib.pyplot as plt
import numpy as np

x=np.array(["A","B","C","D"])
y=np.array([20,50,25,75])

# Yatay çubuklar için width yerine   height   kullanın.(varsayılan 0.8)
#onaltılık renk değerlerinin ikisinde de kullanılabilir
plt.barh(x,y,color='#4CAF50',height=.3)
plt.show()