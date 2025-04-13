DEVICE="cuda"
BATCH_SIZE="32"
# ENTRY='main.py'
MAX_ITER=90
ENTRY='python main.py'  # Change this in your script
# python -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
for TASK in task1 task2 task3
do
    # Train image-only model (DenseNet201)
    CUDA_VISIBLE_DEVICES=0 $ENTRY --model_name "image_only_$TASK" --mode image_only --task $TASK --batch_size $BATCH_SIZE --device $DEVICE --max_iter $MAX_ITER --debug --use_tensorboard 

    # Train text-only model (BERT)
    CUDA_VISIBLE_DEVICES=0 $ENTRY --model_name "text_only_$TASK" --mode text_only --task $TASK --batch_size $BATCH_SIZE --device $DEVICE --max_iter $MAX_ITER --debug --use_tensorboard

    # Combined model
    CUDA_VISIBLE_DEVICES=0 $ENTRY --model_name "full_$TASK" --mode both --task $TASK --batch_size $BATCH_SIZE --device $DEVICE --max_iter $MAX_ITER \
    --image_model_to_load "./output/image_only_$TASK/best.pt"  --text_model_to_load "./output/text_only_$TASK/best.pt" --debug --use_tensorboard 
done

# for TASK in task1 task2 task3
# do
#     # train image-only model (densenet201)
#     CUDA_VISIBLE_DEVICES=0 $ENTRY --model_name "image_only_$TASK" --mode image_only --task $TASK --batch_size $BATCH_SIZE --device $DEVICE --max_iter $MAX_ITER --debug

#     # train text-only model (bert)
#     CUDA_VISIBLE_DEVICES=0 $ENTRY --model_name "text_only_$TASK" --mode text_only --task $TASK --batch_size $BATCH_SIZE --device $DEVICE --max_iter $MAX_ITER --debug 

#     # Combined model
#     CUDA_VISIBLE_DEVICES=0 $ENTRY --model_name "full_$TASK" --mode both --task $TASK --batch_size $BATCH_SIZE --device $DEVICE --max_iter $MAX_ITER \
#     --image_model_to_load "./output/image_only_$TASK/best.pt"  --text_model_to_load "./output/text_only_$TASK/best.pt" --debug
# done