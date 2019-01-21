# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073821.566558
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/courseware/progress_graph.js'
_template_uri = u'/courseware/progress_graph.js'
_source_encoding = 'utf-8'
_exports = []



import bleach
import json
import math

from openedx.core.djangolib.js_utils import (
    dump_js_escaped_json, js_escaped_string
)


def render_body(context,grade_summary,grade_cutoffs,graph_div_id,show_grade_breakdown=True,show_grade_cutoffs=True,**kwargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(show_grade_breakdown=show_grade_breakdown,graph_div_id=graph_div_id,grade_summary=grade_summary,show_grade_cutoffs=show_grade_cutoffs,grade_cutoffs=grade_cutoffs,kwargs=kwargs)
        sorted = context.get('sorted', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n$(function () {\n  function showTooltip(x, y, contents) {\n      $("#tooltip").remove();\n      var $tooltip_div = $(\'<div id="tooltip"></div>\').css({\n          position: \'absolute\',\n          display: \'none\',\n          top: y + 5,\n          left: x + 15,\n          border: \'1px solid #000\',\n          padding: \'4px 6px\',\n          color: \'#fff\',\n          \'background-color\': \'#222\',\n          opacity: 0.90\n      });\n\n      edx.HtmlUtils.setHtml(\n          $tooltip_div,\n          edx.HtmlUtils.HTML(contents)\n      );\n      \n      edx.HtmlUtils.append(\n          $(\'body\'),\n          edx.HtmlUtils.HTML($tooltip_div)\n      );\n      \n      $(\'#tooltip\').fadeIn(200);\n  }\n  /* -------------------------------- Grade detail bars -------------------------------- */\n    \n  ')

        colors = ["#b72121", "#600101", "#666666", "#333333"]
        categories = {}
        
        tickIndex = 1
        sectionSpacer = 0.25
        sectionIndex = 0
        
        ticks = [] #These are the indices and x-axis labels for the data
        bottomTicks = [] #Labels on the bottom
        detail_tooltips = {} #This an dictionary mapping from 'section' -> array of detail_tooltips
        droppedScores = [] #These are the datapoints to indicate assignments which are not factored into the total score
        dropped_score_tooltips = []
        
        for section in grade_summary['section_breakdown']:
            if section.get('prominent', False):
                tickIndex += sectionSpacer
                  
            if section['category'] not in categories:
                colorIndex = len(categories) % len(colors)
                categories[ section['category'] ] = {'label' : section['category'], 
                                                    'data' : [], 
                                                    'color' : colors[colorIndex]}
            
            categoryData = categories[ section['category'] ]
        
            ## Because this is Python (Mako) embedded in JavaScript, our xss linting script is
            ## thoroughly confused. We should rewrite this file to remove Python/Mako.
            ## xss-lint: disable=javascript-jquery-append
            categoryData['data'].append( [tickIndex, section['percent']] )
        
            ## Note that some courses had stored images in the Abbreviation. We are no longer
            ## allowing the display of such images, and remove any previously stored HTML
            ## to prevent ugly HTML from being shown to learners.
            ## xss-lint: disable=javascript-jquery-append
            ticks.append( [tickIndex, bleach.clean(section['label'], tags=[], strip=True)] )
          
            if section['category'] in detail_tooltips:
                ## xss-lint: disable=javascript-jquery-append
                detail_tooltips[ section['category'] ].append( section['detail'] )
            else:
                detail_tooltips[ section['category'] ] = [ section['detail'], ]
                
            if 'mark' in section:
                ## xss-lint: disable=javascript-jquery-append
                droppedScores.append( [tickIndex, 0.05] )
                ## xss-lint: disable=javascript-jquery-append
                dropped_score_tooltips.append( section['mark']['detail'] )
              
            tickIndex += 1
          
            if section.get('prominent', False):
                tickIndex += sectionSpacer
                
        ## ----------------------------- Grade overview bar ------------------------- ##
        tickIndex += sectionSpacer
        
        series = categories.values()
        overviewBarX = tickIndex
        extraColorIndex = len(categories) #Keeping track of the next color to use for categories not in categories[]
        
        if show_grade_breakdown:
          for section in grade_summary['grade_breakdown'].itervalues():
              if section['percent'] > 0:
                  if section['category'] in categories:
                      color = categories[ section['category'] ]['color']
                  else:
                      color = colors[ extraColorIndex % len(colors) ]
                      extraColorIndex += 1
                  ## xss-lint: disable=javascript-jquery-append
                  series.append({
                      'label' : section['category'] + "-grade_breakdown",
                      'data' : [ [overviewBarX, section['percent']] ],
                      'color' : color
                  })
                  
                  detail_tooltips[section['category'] + "-grade_breakdown"] = [ section['detail'] ]
        
          ticks += [ [overviewBarX, "Total"] ]
          tickIndex += 1 + sectionSpacer
        
        totalScore = grade_summary['percent']
        detail_tooltips['Dropped Scores'] = dropped_score_tooltips
        
        
        ## ----------------------------- Grade cutoffs ------------------------- ##
        
        grade_cutoff_ticks = [ [1, "100%"], [0, "0%"] ]
        if show_grade_cutoffs:
          grade_cutoff_ticks = [ [1, "100%"], [0, "0%"] ]
          descending_grades = sorted(grade_cutoffs, key=lambda x: grade_cutoffs[x], reverse=True)
          for grade in descending_grades:
              percent = grade_cutoffs[grade]
              ## xss-lint: disable=javascript-jquery-append
              grade_cutoff_ticks.append( [ percent, u"{0} {1:.0%}".format(grade, percent) ] )
        else:
          grade_cutoff_ticks = [ ]
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['colorIndex','color','series','extraColorIndex','grade_cutoff_ticks','colors','totalScore','sectionSpacer','dropped_score_tooltips','descending_grades','section','ticks','percent','detail_tooltips','grade','bottomTicks','tickIndex','categoryData','categories','sectionIndex','overviewBarX','droppedScores'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n  \n  var series = ')
        __M_writer(dump_js_escaped_json( series ))
        __M_writer(u';\n  var ticks = ')
        __M_writer(dump_js_escaped_json( ticks ))
        __M_writer(u';\n  var bottomTicks = ')
        __M_writer(dump_js_escaped_json( bottomTicks ))
        __M_writer(u';\n  var detail_tooltips = ')
        __M_writer(dump_js_escaped_json( detail_tooltips ))
        __M_writer(u';\n  var droppedScores = ')
        __M_writer(dump_js_escaped_json( droppedScores ))
        __M_writer(u';\n  var grade_cutoff_ticks = ')
        __M_writer(dump_js_escaped_json( grade_cutoff_ticks ))
        __M_writer(u'\n  \n  var yAxisTooltips={};\n\n    /*\n    series looks like:\n    [\n        {\n            color: "#600101",\n            label: "Homework",\n            data: [[1, 0.06666666666666667], [2, 1], [3.25, .53]]\n        },\n        ...\n    ]\n\n    detail_tooltips looks like:\n    {\n        "Dropped Scores": [0: "The lowest 1...:],\n        "Homework": [\n            0: "Homework 1 -- Homework -- Question Styles 7% (1/15)",\n            1: "Homework 2 -- Homework -- Get Social 100% (1/1)",\n            2: "Homework Average = 53%"\n        ],\n        ...\n    }\n    */\n\n  // loop through the series and extract the matching tick and the series label\n  for (var seriesIndex = 0; seriesIndex < series.length; seriesIndex++) {\n      for (var dataIndex = 0; dataIndex < series[seriesIndex][\'data\'].length; dataIndex++) {\n          var tickIndex = series[seriesIndex][\'data\'][dataIndex][0];\n          // There may be more than one detail tooltip for a given tickIndex. If so,\n          // push the new tooltip on the existing list.\n          if (tickIndex in yAxisTooltips) {\n              yAxisTooltips[tickIndex].push(detail_tooltips[series[seriesIndex][\'label\']][dataIndex]);\n          } else {\n              yAxisTooltips[tickIndex] = [detail_tooltips[series[seriesIndex][\'label\']][dataIndex]];\n          }\n          // If this item was a dropped score, add the tooltip message about that.\n          for (var droppedIndex = 0; droppedIndex < droppedScores.length; droppedIndex++) {\n              if (tickIndex === droppedScores[droppedIndex][0]) {\n                  yAxisTooltips[tickIndex].push(detail_tooltips["Dropped Scores"][droppedIndex]);\n              }\n          }\n      }\n  }\n\n  // hide the vertical axis since they are audibly lacking context\n  for (var i = 0; i < grade_cutoff_ticks.length; i++) {\n      grade_cutoff_ticks[i][1] = edx.HtmlUtils.joinHtml(\n          edx.HtmlUtils.HTML(\'<span aria-hidden="true">\'),\n          grade_cutoff_ticks[i][1],\n          edx.HtmlUtils.HTML(\'</span>\')\n      ).text;\n  }\n    \n  //Always be sure that one series has the xaxis set to 2, or the second xaxis labels won\'t show up\n  series.push( {label: \'Dropped Scores\', data: droppedScores, points: {symbol: "cross", show: true, radius: 3}, bars: {show: false}, color: "#333"} );\n  \n  // Allow for arbitrary grade markers e.g. [\'A\', \'B\', \'C\'], [\'Pass\'], etc.\n  var ascending_grades = grade_cutoff_ticks.map(function (el) { return el[0]; }); // Percentage point (in decimal) of each grade cutoff\n  ascending_grades.sort();\n\n  var colors = [\'#f3f3f3\', \'#e9e9e9\', \'#ddd\'];\n  var markings = [];\n  for(var i=1; i<ascending_grades.length-1; i++) // Skip the i=0 marking, which starts from 0%\n    markings.push({yaxis: {from: ascending_grades[i], to: ascending_grades[i+1]}, color: colors[(i-1) % colors.length]});\n\n  var options = {\n    series: {\n        stack: true,\n        lines: {\n            show: false,\n            steps: false\n        },\n        bars: {\n            show: true,\n            barWidth: 0.8,\n            align: \'center\',\n            lineWidth: 0,\n            fill: .8\n        }\n    },\n    xaxis: {\n        tickLength: 0,\n        min: 0.0,\n        max: ')
        __M_writer(dump_js_escaped_json(tickIndex - sectionSpacer ))
        __M_writer(u',\n        ticks: function() {\n            for (var i = 0; i < ticks.length; i++) {\n                var tickLabel = edx.HtmlUtils.joinHtml(\n                    // The very last tick will be for the total, and it usually is composed of a number of different\n                    // grading types. To help clarify, do NOT make the label ("Total") aria-hidden in that case.\n                    edx.HtmlUtils.HTML(i < ticks.length - 1 ? \'<span aria-hidden="true">\' : \'<span>\'),\n                    ticks[i][1],\n                    edx.HtmlUtils.HTML(\'</span>\')\n                );\n                var elementTooltips = yAxisTooltips[ticks[i][0]];\n                if (elementTooltips) {\n                    for (var tooltipIndex = 0; tooltipIndex < elementTooltips.length; tooltipIndex++) {\n                        tickLabel = edx.HtmlUtils.joinHtml(\n                            tickLabel,\n                            edx.HtmlUtils.HTML(\'<span class="sr">\'),\n                            elementTooltips[tooltipIndex],\n                            edx.HtmlUtils.HTML(\'<br></span>\')\n                        );\n                    }\n                }\n                ticks[i][1] = tickLabel;\n            }\n            return ticks;\n        },\n        labelAngle: 90\n    },\n    yaxis: {\n        ticks: grade_cutoff_ticks,\n        min: 0.0,\n        max: 1.0,\n        labelWidth: 100\n    },\n    grid: {\n        hoverable: true,\n        clickable: true,\n        borderWidth: 1,\n        markings: markings\n    },\n    legend: {\n        show: false\n    }\n  };\n  \n  var $grade_detail_graph = $("#')
        __M_writer(js_escaped_string(graph_div_id ))
        __M_writer(u'");\n  if ($grade_detail_graph.length > 0) {\n    var plot = $.plot($grade_detail_graph, series, options);\n    \n')
        if show_grade_breakdown:
            __M_writer(u'      var o = plot.pointOffset(\n          {x: ')
            __M_writer(dump_js_escaped_json(overviewBarX ))
            __M_writer(u' , y: ')
            __M_writer(dump_js_escaped_json(totalScore ))
            __M_writer(u'}\n      );\n\n      edx.HtmlUtils.append(\n          $grade_detail_graph,\n          edx.HtmlUtils.joinHtml(\n              // xss-lint: disable=javascript-concat-html\n              edx.HtmlUtils.HTML(\'<div class="overallGrade" style="position:absolute;left:\' + (o.left - 12) + \'px;top:\' + (o.top - 20) + \'px">\'),\n              edx.HtmlUtils.HTML(\'<span class=sr>\'),\n              gettext(\'Overall Score\'),\n              edx.HtmlUtils.HTML(\'<br></span>\'),\n              \'')
            __M_writer(js_escaped_string('{totalscore:.0%}'.format(totalscore=totalScore) ))
            __M_writer(u"',\n              edx.HtmlUtils.HTML('</div>')\n          )\n      );\n\n")
        __M_writer(u'\n    $grade_detail_graph.find(\'.xAxis .tickLabel\').attr(\'tabindex\', \'0\').focus(function(event) {\n        var $target = $(event.target), srElements = $target.find(\'.sr\'), srText="", i;\n        if (srElements.length > 0) {\n            for (i = 0; i < srElements.length; i++) {\n                srText += srElements[i].innerHTML;\n            }\n            // Position the tooltip slightly above the tick label.\n            showTooltip($target.offset().left - 70, $target.offset().top - 120, srText);\n        }\n    });\n\n    $grade_detail_graph.focusout(function(){\n        $("#tooltip").remove();\n    });\n  }\n  \n      \n  var previousPoint = null;\n  $grade_detail_graph.bind("plothover", function (event, pos, item) {\n    if (item) {\n      if (previousPoint != (item.dataIndex, item.seriesIndex)) {\n        previousPoint = (item.dataIndex, item.seriesIndex);\n            \n        if (item.series.label in detail_tooltips) {\n          var series_tooltips = detail_tooltips[item.series.label];\n          if (item.dataIndex < series_tooltips.length) {\n            showTooltip(item.pageX, item.pageY, series_tooltips[item.dataIndex]);\n          }\n        }\n\n      }\n    } else {\n      $("#tooltip").remove();\n      previousPoint = null;            \n    }\n  });\n});\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"136": 138, "137": 140, "138": 140, "139": 141, "140": 141, "141": 142, "142": 142, "143": 143, "16": 2, "145": 144, "146": 144, "147": 145, "148": 145, "149": 231, "150": 231, "151": 275, "152": 275, "153": 279, "26": 1, "155": 281, "156": 281, "154": 280, "158": 281, "159": 292, "160": 292, "33": 1, "34": 10, "35": 41, "167": 161, "157": 281, "161": 298, "144": 143}, "uri": "/courseware/progress_graph.js", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/courseware/progress_graph.js"}
__M_END_METADATA
"""
