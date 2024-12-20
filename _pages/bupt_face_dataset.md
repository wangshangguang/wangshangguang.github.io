

### About The Dataset
The Bupt_face data set consist of 420 colour images in 21 classes, with 20 images per class.

Users can easily and freely split into training sets and test sets to use.

This data set is the original data set, and the uer can pre-process it, such as face detection.

In addition, we also provide a pre-processed version, see Bupt_face_112x112.mat.

Users can easily scale to the desired ratio, such as 32x32.

### Using The Dataset
The method of using this data set in matlab is as follows:

load Bupt_face.mat;

N1=0.8; % a constant,

[X_trn,Y_trn,X_tst,Y_tst]=sample_random(X_dataset,Y_label,N1,1-N1); % The Bupt_face data set was randomly split into 80% training and 20% testing.

....

If you want to show it, just
for i=1:size(X_dataset,1)
figure;
imshow(reshape(X_dataset(i,:),[112,112]));
end
If you have any questions, please contact me directly.                                                        |


### Download
> [Download](../files/Bupt_face%20dataset.zip)


### Contact Us
Your comments and suggestions are welcome. Please send your comments by email: ctding@bupt.Tedu.Tcn. **We will publish more detailed Call type dataset later.**