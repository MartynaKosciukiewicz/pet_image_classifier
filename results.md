# results
## vgg

```
*** Results Summary for CNN Model Architecture VGG ***
N Images            :  40
N Dog Images        :  30
N Not-Dog Images 10
 
pct_match 87.5
pct_correct_dogs 100.0
pct_correct_breed 93.33333333333333
pct_correct_notdogs 100.0

INCORRECT Dog Breed Assignment:
Real:                     beagle   Classifier:  walker hound, walker foxhound
Real:             great pyrenees   Classifier:                         kuvasz
```
## alexnet

```
*** Results Summary for CNN Model Architecture ALEXNET ***
N Images            :  40
N Dog Images        :  30
N Not-Dog Images 10
 
pct_match 75.0
pct_correct_dogs 100.0
pct_correct_breed 80.0
pct_correct_notdogs 100.0

INCORRECT Dog Breed Assignment:
Real:                     beagle   Classifier:  walker hound, walker foxhound
Real:             boston terrier   Classifier:                        basenji
Real:           golden retriever   Classifier:                tibetan mastiff
Real:           golden retriever   Classifier:                 english setter
Real:             great pyrenees   Classifier:                         kuvasz
Real:           golden retriever   Classifier:           afghan hound, afghan
```

## resnet

```
*** Results Summary for CNN Model Architecture RESNET ***
N Images            :  40
N Dog Images        :  30
N Not-Dog Images 10
 
pct_match 82.5
pct_correct_dogs 100.0
pct_correct_breed 90.0
pct_correct_notdogs 90.0

INCORRECT Dog/NOT Dog Assignments:
cat norwegian elkhound, elkhound

INCORRECT Dog Breed Assignment:
Real:                     beagle   Classifier:  walker hound, walker foxhound
Real:           golden retriever   Classifier:                       leonberg
Real:             great pyrenees   Classifier:                         kuvasz
```

## Conclusions

- **alexnet** infers the fastests results but the accuracy for dog breed detection is the lowest for all of the models used
- **vgg** is the slowest in terms of infering the results, however, it yields the most accurate results
- **resnet** always correctly classifies dogs but has the lowest accuracy for classifying not dogs

