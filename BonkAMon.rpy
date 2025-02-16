init -990 python in mas_submod_utils:
    Submod(
        author="Phazeee",
        name="BonkAMon",
        description="Heh. Bonk your Monika!",
        version="0.0.3"
    )
#====bonk count - submod inspired by Extra+ and OpenWorld heheheheheh.

default persistant.bonk_count = [0, 0, 0]

image zonetwo = im.Scale("mod_assets/other/transparent.png", 180, 120)

#image squeakybat = "submods/BonkAMon/images/bat2.png"

#idle mode from ExtraPlus


image monika staticpose = monika_extraplus


init 5 python:

    monika_extraplus = MASMoniIdleDisp(
        (
            MASMoniIdleExp("1eua", duration=30),
            MASMoniIdleExp("1eubla", duration=30),
            MASMoniIdleExp("1hua", duration=30),
            MASMoniIdleExp("1hubsa", duration=40, aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
            MASMoniIdleExp("1eubsa", duration=40, aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
            MASMoniIdleExp("1eua", duration=30),
            MASMoniIdleExp("1hua", duration=30),
            MASMoniIdleExp("1eubla", duration=40, aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
            MASMoniIdleExp("1esa", duration=30),
            MASMoniIdleExpGroup(
                [
                    MASMoniIdleExp("1eua", duration=30),
                    MASMoniIdleExp("1sua", duration=4),
                    MASMoniIdleExp("1ekblu", duration=40, aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
                    MASMoniIdleExp("1tuu", duration=30),
                    MASMoniIdleExp("1hua", duration=30),
                ]
            ),
            MASMoniIdleExp("1eua_follow", duration=40),
            MASMoniIdleExp("1kua", duration=1),
            MASMoniIdleExp("1eua", duration=30),
            MASMoniIdleExp("1mubla", duration=30, aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
            MASMoniIdleExp("1eubsa", duration=40, aff_range=(mas_aff.ENAMORED, mas_aff.LOVE)),
            MASMoniIdleExp("1huu", duration=30),
        )
    )


init 5 python:
    def bonk_submenu():
        renpy.call_screen("bonk_menu")

init 10001:
    screen mas_extramenu_area():
        zorder 52
        key "e" action Jump("mas_extra_menu_close")
        key "E" action Jump("mas_extra_menu_close")

        frame:
            area(0, 0, 1280, 720)
            background Solid("#0000007F")
        textbutton _("Close"):
                area (60, 596, 120, 35)
                style "hkb_button"
                action Jump("mas_extra_menu_close")
                # zoom control
        frame:
            area (195, 450, 80, 255)
            style "mas_extra_menu_frame"
            vbox:
                spacing 2
                label "Zoom":
                    text_style "mas_extra_menu_label_text"
                    xalign 0.5
                textbutton _("Reset"):
                        style "mas_adjustable_button"
                        selected False
                        xsize 72
                        ysize 35
                        xalign 0.3
                        action SetField(store.mas_sprites, "zoom_level", store.mas_sprites.default_zoom_level)
                bar value FieldValue(store.mas_sprites, "zoom_level", store.mas_sprites.max_zoom):
                    style "mas_adjust_vbar"
                    xalign 0.5
                $ store.mas_sprites.adjust_zoom()
        if store.mas_submod_utils.isSubmodInstalled("Open World"):
                frame:
                    area (310, 639, 202, 65)
                    style "mas_extra_menu_frame"
                    if persistent._mas_in_idle_mode == True:
                        textbutton ("开放世界"):
                            xalign 0.5
                            yalign 0.5
                            action NullAction()
                    else:
                        textbutton ("开放世界"):
                            xalign 0.5
                            yalign 0.5
                            action [Hide("mas_extramenu_area"), Jump("view_OW")] hover_sound gui.hover_sound
                frame:        
                    area (520, 650, 202, 65)
                    style "mas_extra_menu_frame"
                    textbutton ("敲敲莫妮卡"):
                        xalign 0.5
                        yalign 0.5
                        action [Hide("mas_extramenu_area"), Jump("view_bonkmenu")] hover_sound gui.hover_sound           
        else:
            frame:
                area (308, 639, 202, 65)
                style "mas_extra_menu_frame"
                textbutton ("敲敲莫妮卡"):
                    xalign 0.5
                    yalign 0.5
                    action [Hide("mas_extramenu_area"), Jump("view_bonkmenu")] hover_sound gui.hover_sound

screen bonk_menu():
    zorder 50
    style_prefix "hkb"
    hbox:
        grid 2 1:
            spacing 20
            xpos 527
            ypos 534
            textbutton ("敲莫妮卡"): 
                xysize(130, None) 
                action Jump("bonk_a_mon") hover_sound gui.hover_sound
            textbutton ("Return") action Jump("mas_extra_menu_close") hover_sound gui.hover_sound
    vbox: 
        xpos 1166
        ypos 0
        textbutton ("秘密选项") action Jump("DevBaka") hover_sound gui.hover_sound


label view_bonkmenu:
python:
    #mas_RaiseShield_dlg()
    bonk_submenu()
return


#labels land


label show_bonk_screen:
    show monika staticpose at t11
    python:
        store.disable_zoom_button = True
        store.mas_sprites.reset_zoom()
    call screen BonkMain
    return

label BonkMain:

    screen BonkMain():
        zorder 50
        vbox:
            style_prefix "check"
            xpos 1000
            yanchor 1.0
            ypos 260
            label _("可用的\n互动:")
            text _("头") outlines [(2, "#808080", 0, 0)]

        vbox:
            style_prefix "hkb"
            xpos 0.05
            yanchor 1.0
            ypos 90

            #textbutton ("Close") style "hkb_button" action [Hide("extra_gen_list"), Jump("close_boop_screen")]
            textbutton ("Return") style "hkb_button" action [Hide("extra_gen_list"), Jump("zoomfixreturn")]
        #add "submods/BonkAMon/images/bat2.png" xpos 100 ypos 100
        #transform:
        #   zoom 0.1
        imagebutton idle "zonetwo":
            xpos 550 ypos 10
            action [Hide("submod_interactions"), Jump("BonkTime")]
return


label bonk_a_mon:

m "..."
m 6eksdlb "那... 是一个充气球棒吗, [player]?"
m 4rtsdld "啊哈哈，你要拿他干什么?"
#$ mas_HKBDropShield()
jump show_bonk_screen
return

label BonkTime:
    $ persistant.bonk_count[1] += 1
    if persistant.bonk_count[1] == 1:
        m 2efp "啊呜! 你刚刚...敲了我的头吗？!?"
        m 4tuu "我猜我只能敲回去了!"
    elif persistant.bonk_count[1] == 2:
        m 6lfsdrp "唉! [player]!"
        m 5tsa "...你一定很喜欢这个，对吧？"
    elif persistant.bonk_count[1] == 3:
        m 2dfbsa "哎呀！我希望你准备好了，因为一旦我越过[player]，你将承受双倍的痛苦！"
    elif persistant.bonk_count[1] == 4:
        m 6lfp "啊！[player]，我会向你报仇的。"
        m 3nfu "你最好小心点！"
    elif persistant.bonk_count[1] == 5:
        m 4wfp "呜啊！一个充气锤子怎么打人这么疼？？"
        m 2gsp "这不可能呀……"
    elif persistant.bonk_count[1] == 6:
        m 6rtbsu "..."
        m 2ltbfp "..."
        m 3tubfa "哦...只是在想我是否应该买一个更大的球棒...."
        m 5hubfb "开玩笑啦!"
    else:
        $ moldable_variable = renpy.random.randint(1,5)
        if moldable_variable == 1:
            m 7lfblt "哎呀！如果你继续这样下去，我就要扣押你的文件了..."
            m 6tkblu "开玩笑啦， [player]! 我永远不会那么做的."
        elif moldable_variable == 2:
            m 2kksdla "*敲* *敲* *敲*"
            m 7ksb "你真孩子气，[player]... 但我喜欢你这一点。!"
        elif moldable_variable == 3:
            m 6tut "你是一个隐秘的虐待狂吗， [player]?"
            m 5eua "开玩笑啦!"
        elif moldable_variable == 4:
            m 1tkbfb "哎呀！...我猜有人真的想被敲打敲打，是吗？"
            m 7tkbfu "我只是希望你别后悔哦，[player]。"
        elif moldable_variable == 5:
            m 6wfb "嘿!"
    jump show_bonk_screen
return

label MainGaem:
    show monika staticpose at t11
    jump ch30_loop
    return

label DevBaka:

"嗯。。。Bonk a yun。。。我觉得这是某个东西的参考。。。\nps.此mod的灵感来源"

jump ch30_loop
return



label zoomfixreturn:
    $ mas_temp_zoom_level = store.mas_sprites.zoom_level
call monika_zoom_transition_reset(1.0)

call monika_zoom_transition(mas_temp_zoom_level,1.0)
jump ch30_loop

return
