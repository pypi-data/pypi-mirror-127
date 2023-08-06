"""
计算常见机器学习指标的方法
Methods to compute common machine learning metrics
"""
import numpy as np


def _roc_curve(preds, targets, partition, pos_class, neg_class):
    """
    ROC curve (for binary classification only)
    ROC曲线的作用：
    1.较容易地查出任意界限值时的对类别的识别能力
    2.选择最佳的诊断界限值。ROC曲线越靠近左上角,试验的准确性就越高。
        最靠近左上角的ROC曲线的点是错误最少的最好阈值，其假阳性和假阴性的总数最少。
    3.两种或两种以上不同诊断试验对算法性能的比较。
        在对同一种算法的两种或两种以上诊断方法进行比较时，可将各试验的ROC曲线绘制到同一坐标中，以直观地鉴别优劣，
        靠近左上角的ROC曲线所代表的受试者工作最准确。亦可通过分别计算各个试验的ROC曲线下的面积(AUC)进行比较，
        哪一种试验的AUC最大，则哪一种试验的诊断价值最佳。
    """
    thresholds = np.arange(0.0, 1.0, 1.0 / partition)[::-1]
    fpr_list, tpr_list = [], []
    for threshold in thresholds:
        pred_class = (preds >= threshold).astype(int)
        false_pos = np.sum((pred_class == pos_class) & (targets == neg_class))
        fpr_list.append(false_pos / np.sum(targets == neg_class))
        true_pos = np.sum((pred_class == pos_class) & (targets == pos_class))
        tpr_list.append(true_pos / np.sum(targets == pos_class))
    return fpr_list, tpr_list, thresholds


def auc_roc_curve(preds, targets, partition=300, pos_class=1, neg_class=0):
    """
    Area unser the ROC curve (for binary classification only)
    """
    fprs, tprs, thresholds = _roc_curve(preds, targets, partition,
                                        pos_class, neg_class)
    auc_ = 0.0
    for i in range(len(thresholds) - 1):
        auc_ += tprs[i] * (fprs[i + 1] - fprs[i])
    info = {"fprs": fprs, "tprs": tprs, "thresholds": thresholds}
    return auc_, info


def auc(preds, targets, pos_class=1, neg_class=0):
    '''
    AUC（Area Under Curve）被定义为ROC曲线下与坐标轴围成的面积，显然这个面积的数值不会大于1。
    又由于ROC曲线一般都处于y=x这条直线的上方，所以AUC的取值范围在0.5和1之间。AUC越接近1.0，检测方法真实性越高;
    等于0.5时，则真实性最低，无应用价值。
    '''
    num_pos = np.sum(targets == pos_class)
    num_neg = np.sum(targets == neg_class)
    idx = np.argsort(preds, axis=0)
    sorted_targets = targets[idx]
    cnt = 0
    for i, target in enumerate(sorted_targets):
        if target == pos_class:
            cnt += np.sum(sorted_targets[:i] == neg_class)
    auc_ = 1.0 * cnt / (num_pos * num_neg)
    return auc_, {}


def accuracy(preds, targets):
    total_num = len(preds)
    hit_num = int(np.sum(preds == targets))
    accuracy = 1.0 * hit_num / total_num
    info = {"hit_num": hit_num, "total_num": total_num}
    return accuracy, info


def log_loss(preds, targets):
    assert len(preds) == len(targets)
    preds = np.asarray(preds)
    targets = np.asarray(targets)
    log_loss_ = np.mean(-targets * np.log(preds) -
                        (1 - targets) * np.log(1 - preds))
    return log_loss_, {}


def precision(preds, targets, pos_class=1, neg_class=0):
    """
    precision = TP / (TP + FP)
    """
    assert len(preds) == len(targets)
    true_pos = np.sum((preds == pos_class) & (targets == pos_class))
    false_pos = np.sum((preds == pos_class) & (targets == neg_class))
    precision_ = 1. * true_pos / (true_pos + false_pos)
    info = {"true_positive": true_pos, "false_positive": false_pos}
    return precision_, info


def recall(preds, targets, pos_class=1, neg_class=0):
    """
    recall = TP / (TP + FN)
    """
    assert len(preds) == len(targets)
    true_pos = np.sum((preds == pos_class) & (targets == pos_class))
    false_neg = np.sum((preds == neg_class) & (targets == pos_class))
    recall_ = 1. * true_pos / (true_pos + false_neg)
    info = {"true_positive": true_pos, "false_negative": false_neg}
    return recall_, info


def f1_score(preds, targets, pos_class=1, neg_class=0):
    precision_, _ = precision(preds, targets, pos_class, neg_class)
    recall_, _ = recall(preds, targets, pos_class, neg_class)
    f1_ = 2 * (precision_ * recall_) / (precision_ + recall_)
    info = {"precision": precision_, "recall": recall_}
    return f1_, info


def explained_variation(preds, targets):
    """
    Computes fraction of variance that pred_y explains about y.
    Returns 1 - Var[y-pred_y] / Var[y]

    Interpretation:
        EV=0  =>  might as well have predicted zero
        EV=1  =>  perfect prediction
        EV<0  =>  worse than just predicting zero
    """
    assert preds.shape == targets.shape
    if preds.ndim == 1:
        diff_var = np.var(targets - preds)
        target_var = np.var(targets)
        ev_ = 1.0 - diff_var / target_var
    elif preds.ndim == 2:
        diff_var = np.var(targets - preds, axis=0)
        target_var = np.var(targets, axis=0)
        non_zero_idx = np.where(target_var != 0)[0]
        ev_ = np.mean(1.0 - diff_var[non_zero_idx] / target_var[non_zero_idx])
    return ev_, {}


def r_square(preds, targets):
    assert preds.shape == targets.shape
    ss_residual = np.sum((targets - preds) ** 2, axis=0)
    ss_total = np.sum((targets - np.mean(targets, axis=0)) ** 2, axis=0)
    r_square_ = np.mean(1 - ss_residual / ss_total)
    return r_square_, {}


def mean_square_error(preds, targets):
    assert preds.shape == targets.shape
    if preds.ndim == 1:
        mse_ = np.mean(np.square(preds - targets))
    elif preds.ndim == 2:
        mse_ = np.mean(np.sum(np.square(preds - targets), axis=1))
    else:
        raise ValueError("preds supposes to have 1 or 2 dim.")
    return mse_, {}


def mean_absolute_error(preds, targets):
    assert preds.shape == targets.shape
    if preds.ndim == 1:
        mae_ = np.mean(np.abs(preds - targets))
    elif preds.ndim == 2:
        mae_ = np.mean(np.sum(np.abs(preds - targets), axis=1))
    else:
        raise ValueError("preds supposes to have 1 or 2 dim.")
    return mae_, {}
