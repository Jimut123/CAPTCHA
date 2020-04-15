i=0; 
for f in *; 
do 
    d=faded_train_$(printf %03d $((i/64000+1))); 
    mkdir -p $d; 
    mv "$f" $d; 
    let i++; 
done
