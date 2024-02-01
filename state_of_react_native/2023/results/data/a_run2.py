import json

def open_json_file(file_path):
  with open(file_path) as json_file:
    data = json.load(json_file)
    return data

all_responses = 2391
files_data = [
  ('resources__resources_people.json', 'resources_people'),
  ('animations__animations_other.json', 'animations_other'),
  ('component_libraries__component_libraries_other.json', 'component_libraries_other'),
  ('data_fetching__data_fetching_other.json', 'data_fetching_other'),
  ('debugging_and_profiling__debugging_and_profiling_debugging_tools_other.json', 'debugging_and_profiling_debugging_tools_other'),
  ('debugging_and_profiling__debugging_and_profiling_problems_debugging_tools_other.json', 'debugging_and_profiling_problems_debugging_tools_other'),
  ('debugging_and_profiling__debugging_and_profiling_problems_javascript_debugging_features_chrome_dev_tools_other.json', 'debugging_and_profiling_problems_javascript_debugging_features_chrome_dev_tools_other'),
  ('debugging_and_profiling__debugging_and_profiling_problems_javascript_other.json', 'debugging_and_profiling_problems_javascript_other'),
  ('debugging_and_profiling__debugging_and_profiling_profiling_tools_other.json', 'debugging_and_profiling_profiling_tools_other'),
  ('deployment__deployment_other.json', 'deployment_other'),
  ('developer_background_before__developer_background_before_other.json', 'developer_background_before_other'),
  ('developer_background_industry_sector__developer_background_industry_sector_other.json', 'developer_background_industry_sector_other'),
  ('developer_background_platforms__developer_background_platforms_other.json', 'developer_background_platforms_other'),
  ('navigation__navigation_other.json', 'navigation_other'),
  ('opinions__opinions_advantages.json', 'opinions_advantages'),
  ('opinions__opinions_missing.json', 'opinions_missing'),
  ('opinions__opinions_pain_points.json', 'opinions_pain_points'),
  ('platform_apis__platform_apis_other.json', 'platform_apis_other'),
  ('react_native_alternatives__react_native_alternatives_other.json', 'react_native_alternatives_other'),
  ('react_native_app_aspects__react_native_app_aspects_analytics_other.json', 'react_native_app_aspects_analytics_other'),
  ('react_native_app_aspects__react_native_app_aspects_crash_reporting_other.json', 'react_native_app_aspects_crash_reporting_other'),
  ('react_native_app_aspects__react_native_app_aspects_data_visualisation_other.json', 'react_native_app_aspects_data_visualisation_other'),
  ('react_native_app_aspects__react_native_app_aspects_other_libraries_other.json', 'react_native_app_aspects_other_libraries_other'),
  ('react_native_app_aspects__react_native_app_aspects_storage_other.json', 'react_native_app_aspects_storage_other'),
  ('react_native_app_aspects__react_native_app_aspects_testing_other.json', 'react_native_app_aspects_testing_other'),
  ('react_native_specific_features__react_native_features_mobile_web_code_sharing_other.json', 'react_native_features_mobile_web_code_sharing_other'),
  ('react_native_specific_features__react_native_features_ota_updates_other.json', 'react_native_features_ota_updates_other'),
  ('react_native_specific_features__react_native_features_strategies_other.json', 'react_native_features_strategies_other'),
  ('resources__resources_course.json', 'resources_course'),
  ('resources__resources_initially_learn_react_native_other.json', 'resources_initially_learn_react_native_other'),
  ('resources__resources_podcast.json', 'resources_podcast'),
  ('resources__resources_read.json', 'resources_read'),
  ('resources__resources_surveys_other.json', 'resources_surveys_other'),
  ('resources__resources_video.json', 'resources_video'),
  ('state_management__state_management_other.json', 'state_management_other'),
  ('styling__styling_techniques_other.json', 'styling_techniques_other'),
  ('tools__tools_other_tools.json', 'tools_other_tools'),
  ('tools__tools_starter_templates_other.json', 'tools_starter_templates_other'),
]

for file_path, question_key in files_data:
  json_data = open_json_file(file_path)
  new_data = []
  new_keys = []
  chart_percentage = json_data['dataAPI']['survey'][question_key]['all_years'][0]['completion']
  buckets = json_data['dataAPI']['survey'][question_key]['all_years'][0]['facets'][0]['buckets']

  chart_percentage['total'] = all_responses
  chart_percentage['percentage_survey'] = round(chart_percentage['count'] / all_responses * 100, 2)
  for bucket in buckets:
    bucket['percentage_survey'] = round(bucket['count'] / all_responses * 100, 2)

  with open(file_path, 'w') as outfile:
    json.dump(json_data, outfile, indent=2)
