# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073575.935487
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/video.html'
_template_uri = 'video.html'
_source_encoding = 'utf-8'
_exports = []



from django.utils.translation import ugettext as _
from openedx.core.djangolib.js_utils import js_escaped_string


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        display_name = context.get('display_name', UNDEFINED)
        branding_info = context.get('branding_info', UNDEFINED)
        track = context.get('track', UNDEFINED)
        poster = context.get('poster', UNDEFINED)
        transcript_download_formats_list = context.get('transcript_download_formats_list', UNDEFINED)
        handout = context.get('handout', UNDEFINED)
        autoadvance_enabled = context.get('autoadvance_enabled', UNDEFINED)
        cdn_exp_group = context.get('cdn_exp_group', UNDEFINED)
        bumper_metadata = context.get('bumper_metadata', UNDEFINED)
        cdn_eval = context.get('cdn_eval', UNDEFINED)
        transcript_download_format = context.get('transcript_download_format', UNDEFINED)
        download_video_link = context.get('download_video_link', UNDEFINED)
        id = context.get('id', UNDEFINED)
        metadata = context.get('metadata', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        if display_name is not UNDEFINED and display_name is not None:
            __M_writer(u'    <h3 class="hd hd-2">')
            __M_writer(filters.html_escape(filters.decode.utf8(display_name)))
            __M_writer(u'</h3>\n')
        __M_writer(u'\n<div\n    id="video_')
        __M_writer(filters.html_escape(filters.decode.utf8(id)))
        __M_writer(u'"\n    class="video closed"\n    data-metadata=\'')
        __M_writer(filters.html_escape(filters.decode.utf8(metadata)))
        __M_writer(u"'\n    data-bumper-metadata='")
        __M_writer(filters.html_escape(filters.decode.utf8(bumper_metadata)))
        __M_writer(u'\'\n    data-autoadvance-enabled="')
        __M_writer(filters.html_escape(filters.decode.utf8(autoadvance_enabled)))
        __M_writer(u'"\n    data-poster=\'')
        __M_writer(filters.html_escape(filters.decode.utf8(poster)))
        __M_writer(u'\'\n    tabindex="-1"\n>\n    <div class="focus_grabber first"></div>\n\n    <div class="tc-wrapper">\n      <div class="video-wrapper">\n          <span tabindex="0" class="spinner" aria-hidden="false" aria-label="')
        __M_writer(filters.html_escape(filters.decode.utf8(_('Loading video player'))))
        __M_writer(u'"></span>\n          <span tabindex="-1" class="btn-play fa fa-youtube-play fa-2x is-hidden" aria-hidden="true" aria-label="')
        __M_writer(filters.html_escape(filters.decode.utf8(_('Play video'))))
        __M_writer(u'"></span>\n          <div class="video-player-pre"></div>\n          <div class="video-player">\n              <div id="')
        __M_writer(filters.html_escape(filters.decode.utf8(id)))
        __M_writer(u'"></div>\n              <h4 class="hd hd-4 video-error is-hidden">')
        __M_writer(filters.html_escape(filters.decode.utf8(_('No playable video sources found.'))))
        __M_writer(u'</h4>\n              <h4 class="hd hd-4 video-hls-error is-hidden">\n                  ')
        __M_writer(filters.html_escape(filters.decode.utf8(_('Your browser does not support this video format. Try using a different browser.'))))
        __M_writer(u'\n              </h4>\n          </div>\n          <div class="video-player-post"></div>\n          <div class="closed-captions"></div>\n          <div class="video-controls is-hidden">\n              <div>\n                  <div class="vcr"><div class="vidtime">0:00 / 0:00</div></div>\n                  <div class="secondary-controls"></div>\n              </div>\n          </div>\n      </div>\n    </div>\n\n    <div class="focus_grabber last"></div>\n\n')
        if download_video_link or track or handout or branding_info:
            __M_writer(u'    <h3 class="hd hd-4 downloads-heading sr" id="video-download-transcripts_')
            __M_writer(filters.html_escape(filters.decode.utf8(id)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Downloads and transcripts'))))
            __M_writer(u'</h3>\n    <div class="wrapper-downloads" role="region" aria-labelledby="video-download-transcripts_')
            __M_writer(filters.html_escape(filters.decode.utf8(id)))
            __M_writer(u'">\n')
            if download_video_link:
                __M_writer(u'        <div class="wrapper-download-video">\n            <h4 class="hd hd-5">')
                __M_writer(filters.html_escape(filters.decode.utf8(_('Video'))))
                __M_writer(u'</h4>\n            <a class="btn-link video-sources video-download-button" href="')
                __M_writer(filters.html_escape(filters.decode.utf8(download_video_link)))
                __M_writer(u'">\n                ')
                __M_writer(filters.html_escape(filters.decode.utf8(_('Download video file'))))
                __M_writer(u'\n            </a>\n        </div>\n')
            if track:
                __M_writer(u'        <div class="wrapper-download-transcripts">\n            <h4 class="hd hd-5">')
                __M_writer(filters.html_escape(filters.decode.utf8(_('Transcripts'))))
                __M_writer(u'</h4>\n')
                if transcript_download_format:
                    __M_writer(u'            <ul class="list-download-transcripts">\n')
                    for item in transcript_download_formats_list:
                        __M_writer(u'                    <li class="transcript-option">\n                        ')
                        dname = _("Download {file}").format(file=item['display_name']) 
                        
                        __M_locals_builtin_stored = __M_locals_builtin()
                        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['dname'] if __M_key in __M_locals_builtin_stored]))
                        __M_writer(u'\n                        <a class="btn btn-link" href="')
                        __M_writer(filters.html_escape(filters.decode.utf8(track)))
                        __M_writer(u'" data-value="')
                        __M_writer(filters.html_escape(filters.decode.utf8(item['value'])))
                        __M_writer(u'">')
                        __M_writer(filters.html_escape(filters.decode.utf8(dname)))
                        __M_writer(u'</a>\n                    </li>\n')
                    __M_writer(u'            </ul>\n')
                else:
                    __M_writer(u'            <a class="btn-link external-track" href="')
                    __M_writer(filters.html_escape(filters.decode.utf8(track)))
                    __M_writer(u'">')
                    __M_writer(filters.html_escape(filters.decode.utf8(_('Download transcript'))))
                    __M_writer(u'</a>\n')
                __M_writer(u'        </div>\n')
            if handout:
                __M_writer(u'        <div class="wrapper-handouts">\n            <h4 class="hd hd-5">')
                __M_writer(filters.html_escape(filters.decode.utf8(_('Handouts'))))
                __M_writer(u'</h4>\n            <a class="btn-link" href="')
                __M_writer(filters.html_escape(filters.decode.utf8(handout)))
                __M_writer(u'">')
                __M_writer(filters.html_escape(filters.decode.utf8(_('Download Handout'))))
                __M_writer(u'</a>\n        </div>\n')
            if branding_info:
                __M_writer(u'        <div class="branding">\n            <span class="host-tag">')
                __M_writer(filters.html_escape(filters.decode.utf8(branding_info['logo_tag'])))
                __M_writer(u'</span>\n            <a href="')
                __M_writer(filters.html_escape(filters.decode.utf8(branding_info['url'])))
                __M_writer(u'"><img class="brand-logo" src="')
                __M_writer(filters.html_escape(filters.decode.utf8(branding_info['logo_src'])))
                __M_writer(u'" alt="')
                __M_writer(filters.html_escape(filters.decode.utf8(branding_info['logo_tag'])))
                __M_writer(u'" /></a>\n        </div>\n')
            __M_writer(u'    </div>\n')
        __M_writer(u'</div>\n')
        if cdn_eval:
            __M_writer(u'<script>\n  //TODO: refactor this js into a separate file.\n  function sendPerformanceBeacon(id, expgroup, value, event_name) {\n    var data = {event: event_name, id: id, expgroup: expgroup, value: value, page: "html5vid"};\n    $.ajax({method: "POST", url: "/performance", data: data});\n  }\n  var cdnStartTime;\n  var salt = Math.floor((1 + Math.random()) * 0x100000).toString(36);\n  var id = "')
            __M_writer(js_escaped_string(id ))
            __M_writer(u'";\n  function initializeCDNExperiment() {\n    sendPerformanceBeacon(id + "_" + salt, ')
            __M_writer(filters.html_escape(filters.decode.utf8(cdn_exp_group)))
            __M_writer(u', "", "load");\n    cdnStartTime = Date.now();\n    $.each([\'loadstart\', \'abort\', \'error\', \'stalled\', \'loadedmetadata\',\n                    \'loadeddata\', \'canplay\', \'canplaythrough\', \'seeked\'],\n                    function(index, eventName) {\n      $("#video_" + id).bind("html5:" + eventName, null, function() {\n        timeElapsed = Date.now() - cdnStartTime;\n        sendPerformanceBeacon(id + "_" + salt, ')
            __M_writer(filters.html_escape(filters.decode.utf8(cdn_exp_group)))
            __M_writer(u', timeElapsed, eventName);\n      });\n    });\n  }\n  $("#video_" + id).bind("initialize", null, initializeCDNExperiment);\n  if ($("#video_" + id).hasClass("is-initialized")) {\n    initializeCDNExperiment();\n  }\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 3, "21": 1, "40": 1, "41": 6, "42": 7, "43": 8, "44": 8, "45": 8, "46": 10, "47": 12, "48": 12, "49": 14, "50": 14, "51": 15, "52": 15, "53": 16, "54": 16, "55": 17, "56": 17, "57": 24, "58": 24, "59": 25, "60": 25, "61": 28, "62": 28, "63": 29, "64": 29, "65": 31, "66": 31, "67": 47, "68": 48, "69": 48, "70": 48, "71": 48, "72": 48, "73": 49, "74": 49, "75": 50, "76": 51, "77": 52, "78": 52, "79": 53, "80": 53, "81": 54, "82": 54, "83": 58, "84": 59, "85": 60, "86": 60, "87": 61, "88": 62, "89": 63, "90": 64, "91": 65, "95": 65, "96": 66, "97": 66, "98": 66, "99": 66, "100": 66, "101": 66, "102": 69, "103": 70, "104": 71, "105": 71, "106": 71, "107": 71, "108": 71, "109": 73, "110": 75, "111": 76, "112": 77, "113": 77, "114": 78, "115": 78, "116": 78, "117": 78, "118": 81, "119": 82, "120": 83, "121": 83, "122": 84, "123": 84, "124": 84, "125": 84, "126": 84, "127": 84, "128": 87, "129": 89, "130": 90, "131": 91, "132": 99, "133": 99, "134": 101, "135": 101, "136": 108, "137": 108, "143": 137}, "uri": "video.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/video.html"}
__M_END_METADATA
"""
