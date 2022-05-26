a. 

collect natural car images as real images and use them as input for deep-fake model to generate fake images.



b.

GAN will be the first model that I consider, since its architecture is the same as this task. One model intends to fool the other one. The other one try to resist.



c. 

To make model robust, data augmentation is preferred. According to different circumstances, a variety strategies can be chosen. Rotation and flipping can improve robustness generally. Brightness, occlusion and even the cars in different weathers are suitable for images obtained from camera, since those attributes varies over time. Adding gaussian noise to random area is also a way for data augmentation. since the target for model is the artificial images, adversarial examples should be considered. One common example is data added with gaussian noise.



When it comes to out-of-distribution images, the first comes to my mind is Bayesian Neural Network, which performs well in OOD data. If we need solve this by data augmentation, I do not have too much experience on it. In my in shallow opinion, since this task is to detect cars images, which means the OOD data is also cars, but in different brands or types, using data augmentation to force model to focus on part of the cars instead of whole images may be a good to fix this OOD problem. To be specific, most of cars have the same architecture, such as chassis, tyre, lights and so on. Therefore, take slice of semantic parts of cars images as data augmentation is worthy method.