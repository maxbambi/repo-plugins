# -*- coding: utf-8 -*-
"""
    Copyright (C) 2020 Tubed (plugin.video.tubed)

    This file is part of plugin.video.tubed

    SPDX-License-Identifier: GPL-2.0-only
    See LICENSES/GPL-2.0-only.txt for more information.
"""

from ..dialogs.autoplay_related import AutoplayRelated
from ..dialogs.common import open_dialog
from ..dialogs.sign_in import SignInDialog


def invoke(context, dialog_id):
    if dialog_id == 'autoplay_related':
        _ = open_dialog(context, AutoplayRelated, mode='demo')

    elif dialog_id == 'sign_in':
        _ = open_dialog(context, SignInDialog, mode='demo')
