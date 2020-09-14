checkpoint_config = dict(interval=1)
# yapf:disable
log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook'),
        # dict(type='TensorboardLoggerHook')
    ])
# yapf:enable
dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = '/nfs/volume-364-1/xuzhenhao/Z.backup/mmdet_weight/mmdetv2.3.0/faster_rcnn_r50_fpn_mdconv_c3-c5_1x_coco_20200130-d099253b.pth'
resume_from = None
workflow = [('train', 1)]
