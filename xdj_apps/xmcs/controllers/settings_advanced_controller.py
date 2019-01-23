import xdj
from xdj_apps.xmcs.controllers.commons import CommonController
@xdj.Controller(
    url="settings/advanced",
    template="settings/advanced.html",
    check_url_=r"^settings/advanced/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)$",
    replace_url =r"^settings/advanced/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)$"
)
class SettingsAdvancedController(CommonController):
    def on_get(self,model):
        course = self.__get_course_ware_from_str_key__(model.params.course_key_string,model.user)
        model.course = course
        fields = dict(
            display_name=dict(
                caption="Course Display Name",
                type="text",
                description="Enter the name of the course as it should appear in the edX.org course list."
            ),
            advanced_modules=dict(
                caption="Advanced Module List",
                type="list",
                description ="Enter the names of the advanced modules to use in your course."

            ),

            allow_anonymous=dict(
                caption="Allow Anonymous Discussion Posts",
                type="bool",
                description="Enter true or false. If true, students can create discussion posts that are anonymous to all users."
            ),
            allow_anonymous_to_peers=dict(
                caption="Allow Anonymous Discussion Posts to Peers",
                type="bool",
                description="Enter true or false. If true, students can create discussion posts that are anonymous to other students. "
                            "This setting does not make posts anonymous to course staff."
            ),
            allow_proctoring_opt_out=dict(
                caption="Allow Opting Out of Proctored Exams",
                type="bool",
                description="Enter true or false. If this value is true, learners can choose to take proctored exams without proctoring. "
                            "If this value is false, all learners must take the exam with proctoring. "
                            "This setting only applies if proctored exams are enabled for the course."
            ),
            allow_public_wiki_access=dict(
                caption="Allow Public Wiki Access",
                type="bool",
                description="Enter true or false. If true, edX users can view the course wiki even if they're not enrolled in the course."
            ),

            cert_name_long=dict(
                caption="Certificate Name (Long)",
                type="text",
                description="Use this setting only when generating PDF certificates. Between quotation marks, "
                            "enter the long name of the type of certificate that students receive when they complete the course. "
                            "For instance, ""Certificate of Achievement""."
            ),
            cert_name_short=dict(
                caption="Certificate Name (Short)",
                type="list",
                description="Use this setting only when generating PDF certificates. Between quotation marks, "
                            "enter the short name of the type of certificate that students receive when they complete the course. "
                            "For instance, ""Certificate""."
            ),
            cert_html_view_overrides=dict(
                caption="Certificate Web/HTML View Overrides",
                type="list",
                description="Enter course-specific overrides for the Web/HTML template parameters here (JSON format)"
            ),
            certificates_display_behavior=dict(
                caption="Certificates Display Behavior",
                type="list",
                description="Enter end, early_with_info, or early_no_info. After certificate generation, "
                            "students who passed see a link to their certificates on the dashboard and "
                            "students who did not pass see information about the grading configuration. "
                            "The default is end, which displays this certificate information to all students after the course end date. "
                            "To display this certificate information to all students as soon as certificates are generated, "
                            "enter early_with_info. To display only the links to passing students as soon as certificates are generated, "
                            "enter early_no_info."
            ),

            cosmetic_display_price=dict(
                caption="Cosmetic Course Display Price",
                type="list",
                description="The cost displayed to students for enrolling in the course. "
                            "If a paid course registration price is set by an administrator in the database, "
                            "that price will be displayed instead of this one."
            ),
            course_image=dict(
                caption="Course About Page Image",
                type="list",
                description="Edit the name of the course image file. "
                            "You must upload this file on the Files & Uploads page. "
                            "You can also set the course image on the Settings & Details page."
            ),
            advertised_start=dict(
                caption="Course Advertised Start",
                type="list",
                description="Enter the text that you want to use as the advertised starting time frame for the course, such as ""Winter 2018"". "
                            "If you enter null for this value, the start date that you have set for this course is used."
            ),
            banner_image=dict(
                caption="Course Banner Image",
                type="list",
                description="Edit the name of the banner image file. You can set the banner image on the Settings & Details page."
            ),

            instructor_info=dict(
                caption="Course Instructor",
                type="list",
                description="Enter the details for Course Instructor"
            ),
            is_new=dict(
                caption="Course Is New",
                type="list",
                description="Enter true or false. If true, the course appears in the list of new courses on edx.org, "
                            "and a New! badge temporarily appears next to the course image."
            ),

            learning_info=dict(
                caption="Course Learning Information",
                type="list",
                description="Specify what student can learn from the course."
            ),
            max_student_enrollments_allowed=dict(
                caption="Course Maximum Student Enrollment",
                type="number",
                description="Enter the maximum number of students that can enroll in the course. "
                            "To allow an unlimited number of students, enter null."
            ),
            disable_progress_graph=dict(
                caption="Disable Progress Graph",
                type="bool",
                description="Enter true or false. If true, students cannot view the progress graph."
            ),

            discussion_blackouts=dict(
                caption="Discussion Blackout Dates",
                type="dates",
                description="Enter pairs of dates between which students cannot post to discussion forums. "
                            "Inside the provided brackets, enter an additional set of square brackets "
                            "surrounding each pair of dates you add. Format each pair of dates as [""YYYY-MM-DD"", ""YYYY-MM-DD""]."
                            "To specify times as well as dates, format each pair as [""YYYY-MM-DDTHH:MM"", ""YYYY-MM-DDTHH:MM""]. "
                            "Be sure to include the ""T"" between the date and time. For example, an entry defining two blackout periods looks like this, "
                            "including the outer pair of square brackets: [[""2015-09-15"", ""2015-09-21""], [""2015-10-01"", ""2015-10-08""]]"
            ),

            discussion_sort_alpha=dict(
                caption="Discussion Sorting Alphabetical",
                type="list",
                description="Enter true or false. If true, discussion categories and subcategories are sorted alphabetically. "
                            "If false, they are sorted chronologically by creation date and time."
            ),

            due_date_display_format=dict(
                caption="Due Date Display Format",
                type="list",
                description="Enter the format for due dates. The default is Mon DD, YYYY. "
                            "Enter ""%m-%d-%Y"" for MM-DD-YYYY, ""%d-%m-%Y"" for DD-MM-YYYY"
                            ", ""%Y-%m-%d"" for YYYY-MM-DD, or ""%Y-%d-%m"" for YYYY-DD-MM."
            ),
            use_latex_compiler=dict(
                caption="Enable LaTeX Compiler",
                type="list",
                description="Enter true or false. "
                            "If true, you can use the LaTeX templates for HTML components and advanced Problem components."
            ),

            enable_proctored_exams=dict(
                caption="Enable Proctored Exams",
                type="list",
                description="Enter true or false. If this value is true, "
                            "proctored exams are enabled in your course. "
                            "Note that enabling proctored exams will also enable timed exams."
            ),
            enable_subsection_gating=dict(
                caption="Enable Subsection Prerequisites",
                type="list",
                description="Enter true or false. If this value is true, you can hide a subsection until "
                            "learners earn a minimum score in another, prerequisite subsection."
            ),
            enable_timed_exams=dict(
                caption="Enable Timed Exams",
                type="list",
                description="Enter true or false. If this value is true, "
                            "timed exams are enabled in your course. Regardless of this setting, "
                            "timed exams are enabled if Enable Proctored Exams is set to true."
            ),
            html_textbooks=dict(
                caption="HTML Textbooks",
                type="list",
                description="For HTML textbooks that appear as separate tabs in the course, "
                            "enter the name of the tab (usually the title of the book) as well as "
                            "the URLs and titles of each chapter in the book."
            ),
            due=dict(
                caption="Due Date",
                type="list",
                description="Enter the date by which problems are due."
            ),
            invitation_only=dict(
                caption="Invitation Only",
                type="list",
                description="Whether to restrict enrollment to invitation by the course staff."
            ),
            max_attempts=dict(
                caption="Maximum Attempts",
                type="list",
                description="Enter the maximum number of times a student can try to answer problems. "
                            "By default, Maximum Attempts is set to null, "
                            "meaning that students have an unlimited number of attempts for problems. "
                            "You can override this course-wide setting for individual problems. "
                            "However, if the course-wide setting is a specific number, "
                            "you cannot set the Maximum Attempts for individual problems to unlimited."
            ),
            rerandomize=dict(
                caption="Randomization",
                type="list",
                description="Specify the default for how often variable values in a problem are randomized. "
                            "This setting should be set to ""never"" unless you plan to provide a "
                            "Python script to identify and randomize values in most of the problems in your course. "
                            "Valid values are ""always"", ""onreset"", ""never"", and ""per_student""."
            )
        )
        ng_data = {}
        model.fields=[]
        for k,v in fields.items():
            model.fields.append(k)
            model.fieldInfo=fields
            ng_data.update({
                k : getattr(course,k)
            })
        model.ng_data=ng_data
        return self.render(model)
    def on_post(self,model):
        return xdj.Handler(model)