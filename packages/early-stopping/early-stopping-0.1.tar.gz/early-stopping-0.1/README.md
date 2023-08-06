# Early Stopping
---
I'm too lazy to read the Tensorflow documentation, so I made this simple early stopper. After each training step, feed the object the testing loss result for that epoch and it will return a boolean that says whether or not to break the training loop. 

**Example usage:**

```py
from early_stopping import EarlyStopping

early_stopper = EarlyStopping(
    depth=5,
    ignore=20,
    method='consistency'
)

# Your training loop
for epoch in range(EPOCHS):
    # Train step here
    # Test step here

    # Check if we should break the loop
    if early_stopper.check(testing_loss):
        print('BREAKING THE TRAINING LOOP')
        break

```