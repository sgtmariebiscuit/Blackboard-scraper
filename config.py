import getpass
user = getpass.getuser()

blackboard_login = "https://cas.uj.ac.za/cas-server-webapp-3.5.2/login?service=https%3A%2F%2Fuj.blackboard.com%2Fwebapps%2Fbb-auth-provider-cas-BB5c04f198cda22%2Fexecute%2FcasLogin%3Fcmd%3Dlogin%26authProviderId%3D_125_1%26redirectUrl%3Dhttps%253A%252F%252Fuj.blackboard.com%252Fultra&renew=true"
blackboard_courses = "https://uj.blackboard.com/ultra/course"
blackboard_BMA = "https://uj.blackboard.com/ultra/courses/_29749_1/cl/outline"
blackbaord_ILS ="https://uj.blackboard.com/ultra/courses/_32265_1/cl/outline"
blackboard_DEV ="https://uj.blackboard.com/ultra/courses/_32561_1/cl/outline"
blackboard_DEV_labs ="https://uj.blackboard.com/webapps/blackboard/content/listContent.jsp?course_id=_32561_1&content_id=_2008069_1&mode=reset"
blackboard_DEV_tuts = "https://uj.blackboard.com/webapps/blackboard/content/listContent.jsp?course_id=_32561_1&content_id=_2003716_1&mode=reset"
blackboard_DEV_Submission_labs="https://uj.blackboard.com/webapps/blackboard/content/listContent.jsp?course_id=_32561_1&content_id=_2008106_1&mode=reset"
blackboard_DEV_Submission_tuts="https://uj.blackboard.com/webapps/blackboard/content/listContent.jsp?course_id=_32561_1&content_id=_2005687_1&mode=reset"



# Add your own information to these variables
path = (f'/home/{user}/Downloads/') #Specifies default directory where your downloads will go
username = ""
password = ""
