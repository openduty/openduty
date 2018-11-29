--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.5
-- Dumped by pg_dump version 10.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: accounts_token; Type: TABLE DATA; Schema: public; Owner: openduty
--

INSERT INTO public.accounts_token (key, created) VALUES ('qwertyuiop', '2018-11-26 15:49:59.102852+00');
INSERT INTO public.accounts_token (key, created) VALUES ('4bb275bcb4ca991da2dff78e548278c890ed6f96', '2018-11-26 16:18:12.910669+00');
INSERT INTO public.accounts_token (key, created) VALUES ('cda95a1a396ddf028d040355a534e746e980ce6d', '2018-11-26 16:18:28.888884+00');
INSERT INTO public.accounts_token (key, created) VALUES ('0aa8fe734605e984500df39f756fc925af1b46e4', '2018-11-26 16:18:31.396802+00');


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: openduty
--

INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (1, 'pbkdf2_sha256$120000$IvDAiB0mm2xj$Z1v52Zwhfu5tIatYprsC2IS+tIL0Y1UmDSqSkevdLpg=', '2018-11-26 15:48:24+00', true, 'demo', 'Demo', 'User', 'demo@openduty.com', true, true, '2018-11-26 15:46:53+00');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (2, 'pbkdf2_sha256$120000$p7K5dTgl8OuX$6OMNa2+HrZy1geEkCjNMbP3Lj3WdaVPOEV87Bgbld80=', NULL, false, 'demo2', 'Demo2', 'User2', 'demo2@openduty.com', true, true, '2018-11-26 21:47:32+00');


--
-- Data for Name: accounts_userprofile; Type: TABLE DATA; Schema: public; Owner: openduty
--

INSERT INTO public.accounts_userprofile (id, phone_number, pushover_user_key, pushover_app_key, slack_room_name, prowl_api_key, prowl_application, prowl_url, rocket_webhook_url, hipchat_room_name, hipchat_room_url, send_resolve_enabled, user_id) VALUES (1, '+41764744645', 'qwertyuiop', 'qwertyuiop', 'qwertyuiop', 'qwertyuiop', 'qwertyuiop', 'qwertyuiop', 'qwertyuiop', 'qwertyuiop', 'qwertyuiop', true, 1);
INSERT INTO public.accounts_userprofile (id, phone_number, pushover_user_key, pushover_app_key, slack_room_name, prowl_api_key, prowl_application, prowl_url, rocket_webhook_url, hipchat_room_name, hipchat_room_url, send_resolve_enabled, user_id) VALUES (2, '+44764744645', 'qwertyuiop', 'qwertyuiop', 'qwertyuiop', 'qwertyuiop', 'qwertyuiop', 'qwertyuiop', 'qwertyuiop', 'qwertyuiop', 'qwertyuiop', true, 2);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: openduty
--

INSERT INTO public.auth_group (id, name) VALUES (1, 'Demo Group');


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: openduty
--

INSERT INTO public.django_content_type (id, app_label, model) VALUES (1, 'admin', 'logentry');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (2, 'auth', 'permission');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (3, 'auth', 'group');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (4, 'auth', 'user');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (6, 'sessions', 'session');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (7, 'django_celery_beat', 'crontabschedule');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (8, 'django_celery_beat', 'intervalschedule');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (9, 'django_celery_beat', 'periodictask');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (10, 'django_celery_beat', 'periodictasks');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (11, 'django_celery_beat', 'solarschedule');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (12, 'django_twilio', 'caller');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (13, 'django_twilio', 'credential');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (14, 'schedule', 'calendar');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (15, 'schedule', 'calendarrelation');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (16, 'schedule', 'event');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (17, 'schedule', 'eventrelation');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (18, 'schedule', 'occurrence');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (19, 'schedule', 'rule');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (20, 'accounts', 'token');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (21, 'accounts', 'userprofile');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (22, 'events', 'eventlog');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (23, 'incidents', 'incident');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (24, 'incidents', 'incidentsilenced');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (25, 'notification', 'schedulednotification');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (26, 'notification', 'usernotificationmethod');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (27, 'policies', 'schedulepolicy');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (28, 'policies', 'schedulepolicyrule');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (29, 'schedules', 'schedulepolicy');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (30, 'schedules', 'schedulepolicyrule');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (31, 'services', 'service');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (32, 'services', 'servicesilenced');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (33, 'services', 'servicetokens');


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: openduty
--

INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (25, 'Can add crontab', 7, 'add_crontabschedule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (26, 'Can change crontab', 7, 'change_crontabschedule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (27, 'Can delete crontab', 7, 'delete_crontabschedule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (28, 'Can view crontab', 7, 'view_crontabschedule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (29, 'Can add interval', 8, 'add_intervalschedule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (30, 'Can change interval', 8, 'change_intervalschedule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (31, 'Can delete interval', 8, 'delete_intervalschedule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (32, 'Can view interval', 8, 'view_intervalschedule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (33, 'Can add periodic task', 9, 'add_periodictask');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (34, 'Can change periodic task', 9, 'change_periodictask');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (35, 'Can delete periodic task', 9, 'delete_periodictask');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (36, 'Can view periodic task', 9, 'view_periodictask');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (37, 'Can add periodic tasks', 10, 'add_periodictasks');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (38, 'Can change periodic tasks', 10, 'change_periodictasks');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (39, 'Can delete periodic tasks', 10, 'delete_periodictasks');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (40, 'Can view periodic tasks', 10, 'view_periodictasks');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (41, 'Can add solar event', 11, 'add_solarschedule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (42, 'Can change solar event', 11, 'change_solarschedule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (43, 'Can delete solar event', 11, 'delete_solarschedule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (44, 'Can view solar event', 11, 'view_solarschedule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (45, 'Can add caller', 12, 'add_caller');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (46, 'Can change caller', 12, 'change_caller');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (47, 'Can delete caller', 12, 'delete_caller');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (48, 'Can view caller', 12, 'view_caller');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (49, 'Can add credential', 13, 'add_credential');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (50, 'Can change credential', 13, 'change_credential');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (51, 'Can delete credential', 13, 'delete_credential');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (52, 'Can view credential', 13, 'view_credential');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (53, 'Can add calendar', 14, 'add_calendar');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (54, 'Can change calendar', 14, 'change_calendar');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (55, 'Can delete calendar', 14, 'delete_calendar');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (56, 'Can view calendar', 14, 'view_calendar');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (57, 'Can add calendar relation', 15, 'add_calendarrelation');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (58, 'Can change calendar relation', 15, 'change_calendarrelation');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (59, 'Can delete calendar relation', 15, 'delete_calendarrelation');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (60, 'Can view calendar relation', 15, 'view_calendarrelation');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (61, 'Can add event', 16, 'add_event');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (62, 'Can change event', 16, 'change_event');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (63, 'Can delete event', 16, 'delete_event');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (64, 'Can view event', 16, 'view_event');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (65, 'Can add event relation', 17, 'add_eventrelation');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (66, 'Can change event relation', 17, 'change_eventrelation');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (67, 'Can delete event relation', 17, 'delete_eventrelation');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (68, 'Can view event relation', 17, 'view_eventrelation');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (69, 'Can add occurrence', 18, 'add_occurrence');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (70, 'Can change occurrence', 18, 'change_occurrence');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (71, 'Can delete occurrence', 18, 'delete_occurrence');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (72, 'Can view occurrence', 18, 'view_occurrence');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (73, 'Can add rule', 19, 'add_rule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (74, 'Can change rule', 19, 'change_rule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (75, 'Can delete rule', 19, 'delete_rule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (76, 'Can view rule', 19, 'view_rule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (77, 'Can add token', 20, 'add_token');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (78, 'Can change token', 20, 'change_token');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (79, 'Can delete token', 20, 'delete_token');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (80, 'Can view token', 20, 'view_token');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (81, 'Can add user profile', 21, 'add_userprofile');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (82, 'Can change user profile', 21, 'change_userprofile');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (83, 'Can delete user profile', 21, 'delete_userprofile');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (84, 'Can view user profile', 21, 'view_userprofile');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (85, 'Can add eventlog', 22, 'add_eventlog');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (86, 'Can change eventlog', 22, 'change_eventlog');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (87, 'Can delete eventlog', 22, 'delete_eventlog');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (88, 'Can view eventlog', 22, 'view_eventlog');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (89, 'Can add incidents', 23, 'add_incident');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (90, 'Can change incidents', 23, 'change_incident');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (91, 'Can delete incidents', 23, 'delete_incident');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (92, 'Can view incidents', 23, 'view_incident');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (93, 'Can add incident silenced', 24, 'add_incidentsilenced');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (94, 'Can change incident silenced', 24, 'change_incidentsilenced');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (95, 'Can delete incident silenced', 24, 'delete_incidentsilenced');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (96, 'Can view incident silenced', 24, 'view_incidentsilenced');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (97, 'Can add scheduled_notifications', 25, 'add_schedulednotification');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (98, 'Can change scheduled_notifications', 25, 'change_schedulednotification');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (99, 'Can delete scheduled_notifications', 25, 'delete_schedulednotification');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (100, 'Can view scheduled_notifications', 25, 'view_schedulednotification');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (101, 'Can add user_notification_method', 26, 'add_usernotificationmethod');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (102, 'Can change user_notification_method', 26, 'change_usernotificationmethod');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (103, 'Can delete user_notification_method', 26, 'delete_usernotificationmethod');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (104, 'Can view user_notification_method', 26, 'view_usernotificationmethod');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (105, 'Can add schedule_policy', 27, 'add_schedulepolicy');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (106, 'Can change schedule_policy', 27, 'change_schedulepolicy');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (107, 'Can delete schedule_policy', 27, 'delete_schedulepolicy');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (108, 'Can view schedule_policy', 27, 'view_schedulepolicy');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (109, 'Can add schedule_policy_rule', 28, 'add_schedulepolicyrule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (110, 'Can change schedule_policy_rule', 28, 'change_schedulepolicyrule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (111, 'Can delete schedule_policy_rule', 28, 'delete_schedulepolicyrule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (112, 'Can view schedule_policy_rule', 28, 'view_schedulepolicyrule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (113, 'Can add schedule_policy', 29, 'add_schedulepolicy');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (114, 'Can change schedule_policy', 29, 'change_schedulepolicy');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (115, 'Can delete schedule_policy', 29, 'delete_schedulepolicy');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (116, 'Can view schedule_policy', 29, 'view_schedulepolicy');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (117, 'Can add schedule_policy_rule', 30, 'add_schedulepolicyrule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (118, 'Can change schedule_policy_rule', 30, 'change_schedulepolicyrule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (119, 'Can delete schedule_policy_rule', 30, 'delete_schedulepolicyrule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (120, 'Can view schedule_policy_rule', 30, 'view_schedulepolicyrule');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (121, 'Can add service', 31, 'add_service');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (122, 'Can change service', 31, 'change_service');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (123, 'Can delete service', 31, 'delete_service');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (124, 'Can view service', 31, 'view_service');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (125, 'Can add service silenced', 32, 'add_servicesilenced');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (126, 'Can change service silenced', 32, 'change_servicesilenced');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (127, 'Can delete service silenced', 32, 'delete_servicesilenced');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (128, 'Can view service silenced', 32, 'view_servicesilenced');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (129, 'Can add service_tokens', 33, 'add_servicetokens');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (130, 'Can change service_tokens', 33, 'change_servicetokens');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (131, 'Can delete service_tokens', 33, 'delete_servicetokens');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (132, 'Can view service_tokens', 33, 'view_servicetokens');


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: openduty
--



--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: openduty
--

INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (1, 1, 1);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (2, 2, 1);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: openduty
--



--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: openduty
--

INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (1, '2018-11-26 15:49:47.906564+00', '1', 'UserProfile object (1)', 1, '[{"added": {}}]', 21, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (2, '2018-11-26 15:49:59.104197+00', 'qwertyuiop', 'qwertyuiop', 1, '[{"added": {}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (3, '2018-11-26 15:50:15.073161+00', '1', '+41764744645', 1, '[{"added": {}}]', 12, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (4, '2018-11-26 15:50:29.018017+00', '1', 'demo - qwertyuiop', 1, '[{"added": {}}]', 13, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (5, '2018-11-26 15:51:29.828802+00', '1', 'Demo Schedule Policy 1', 1, '[{"added": {}}]', 29, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (6, '2018-11-26 15:51:41.901184+00', '2', 'Demo Schedule Policy 3', 1, '[{"added": {}}]', 29, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (7, '2018-11-26 15:51:52.142217+00', '3', 'Demo Schedule Policy  2', 1, '[{"added": {}}]', 29, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (8, '2018-11-26 15:52:11.694744+00', '2', 'Demo Schedule Policy2', 2, '[{"changed": {"fields": ["name"]}}]', 29, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (9, '2018-11-26 15:52:19.925731+00', '3', 'Demo Schedule Policy  3', 2, '[{"changed": {"fields": ["name", "repeat_times"]}}]', 29, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (10, '2018-11-26 15:52:24.710523+00', '2', 'Demo Schedule Policy 2', 2, '[{"changed": {"fields": ["name"]}}]', 29, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (11, '2018-11-26 15:52:42.812769+00', 'acaede8f-1f05-4d9b-a9e2-747d4140eabf', 'Demo Service key 1', 1, '[{"added": {}}]', 31, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (12, '2018-11-26 15:53:22.711098+00', 'ebc956ad-5f0f-4385-8781-9290e4e06902', 'Demo Service key 2', 1, '[{"added": {}}]', 31, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (13, '2018-11-26 15:53:55.265137+00', '2b1e704d-616d-48a6-bfbf-a73382c69deb', 'Demo Service key 3', 1, '[{"added": {}}]', 31, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (14, '2018-11-26 15:54:59.716885+00', '1a32b4c9-6ce3-4c0f-a734-046b4c8bdf6f', 'Demo Service 1', 1, '[{"added": {}}]', 31, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (15, '2018-11-26 15:55:34.466675+00', '1', 'qwerty1', 1, '[{"added": {}}]', 23, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (16, '2018-11-26 15:56:25.069339+00', '7bece19f-057e-4db8-b6a4-5275b6c916d9', 'Demo Service 2', 1, '[{"added": {}}]', 31, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (17, '2018-11-26 15:56:29.668895+00', '1', 'Some demo data about this Event', 1, '[{"added": {}}]', 22, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (18, '2018-11-26 20:28:12.623997+00', '1', 'Rule Schedule Rule 1 params Demo content description about Schedule Rule 1', 1, '[{"added": {}}]', 19, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (19, '2018-11-26 20:28:24.846336+00', '1', 'Event 1: Nov. 26, 2018 - Nov. 27, 2018', 1, '[{"added": {}}]', 16, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (20, '2018-11-26 21:04:06.164748+00', '1', 'Demo Group', 1, '[{"added": {}}]', 3, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (21, '2018-11-26 21:04:27.213775+00', '1', 'demo', 2, '[{"changed": {"fields": ["first_name", "last_name", "groups"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (22, '2018-11-26 21:11:25.196285+00', '2', 'Rule Rule 2 params a = 2', 1, '[{"added": {}}]', 19, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (23, '2018-11-26 21:12:02.046779+00', '2', 'Event 2: Nov. 26, 2018 - Dec. 20, 2018', 1, '[{"added": {}}]', 16, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (24, '2018-11-26 21:39:10.386583+00', '3', 'demo,demo: Nov. 28, 2018 - Nov. 29, 2018', 2, '[{"changed": {"fields": ["color_event", "calendar"]}}]', 16, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (25, '2018-11-26 21:39:22.230672+00', '3', 'Demo 2: Nov. 28, 2018 - Nov. 29, 2018', 2, '[{"changed": {"fields": ["title"]}}]', 16, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (26, '2018-11-26 21:40:53.808705+00', '3', 'demo, demo: Nov. 28, 2018 - Nov. 29, 2018', 2, '[{"changed": {"fields": ["title"]}}]', 16, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (27, '2018-11-26 21:41:21.811351+00', '2', 'Event 2: Nov. 26, 2018 - Dec. 20, 2018', 2, '[{"changed": {"fields": ["creator"]}}]', 16, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (28, '2018-11-26 21:43:54.404499+00', '2', 'Event 2: Nov. 28, 2018 - Dec. 29, 2018', 2, '[{"changed": {"fields": ["start", "end", "creator"]}}]', 16, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (29, '2018-11-26 21:44:16.499212+00', '3', 'demo, demo: Nov. 27, 2018 - Nov. 28, 2018', 2, '[{"changed": {"fields": ["start", "end", "calendar"]}}]', 16, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (30, '2018-11-26 21:47:52.987577+00', '2', 'demo2', 2, '[{"changed": {"fields": ["is_superuser"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (31, '2018-11-26 21:48:20.353045+00', '2', 'demo2', 2, '[{"changed": {"fields": ["first_name", "last_name", "groups"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (32, '2018-11-26 21:49:10.073107+00', '2', 'UserProfile object (2)', 1, '[{"added": {}}]', 21, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (33, '2018-11-26 21:52:23.277052+00', '2', '+40764744645', 1, '[{"added": {}}]', 12, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (34, '2018-11-26 21:52:39.822091+00', '2', 'demo2 - qwertyuiop', 1, '[{"added": {}}]', 13, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (35, '2018-11-26 21:53:10.538438+00', '2', 'The password is too similar to the email address.
This password is too short. It must contain at least 8 characters.', 1, '[{"added": {}}]', 22, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (36, '2018-11-26 21:53:35.242361+00', '3', 'The password is too similar to the email address.
This password is too short. It must contain at least 8 characters.', 1, '[{"added": {}}]', 22, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (37, '2018-11-26 21:53:56.25153+00', '4', 'The password is too similar to the email address.', 1, '[{"added": {}}]', 22, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (38, '2018-11-26 21:54:47.35401+00', '5', 'GRANT ALL ON SCHEMA public TO PUBLIC;', 1, '[{"added": {}}]', 22, 1);


--
-- Data for Name: django_celery_beat_crontabschedule; Type: TABLE DATA; Schema: public; Owner: openduty
--



--
-- Data for Name: django_celery_beat_intervalschedule; Type: TABLE DATA; Schema: public; Owner: openduty
--



--
-- Data for Name: django_celery_beat_solarschedule; Type: TABLE DATA; Schema: public; Owner: openduty
--



--
-- Data for Name: django_celery_beat_periodictask; Type: TABLE DATA; Schema: public; Owner: openduty
--



--
-- Data for Name: django_celery_beat_periodictasks; Type: TABLE DATA; Schema: public; Owner: openduty
--



--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: openduty
--

INSERT INTO public.django_migrations (id, app, name, applied) VALUES (1, 'contenttypes', '0001_initial', '2018-11-26 15:45:51.513256+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (2, 'auth', '0001_initial', '2018-11-26 15:45:51.562741+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (3, 'accounts', '0001_initial', '2018-11-26 15:45:51.584505+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (4, 'admin', '0001_initial', '2018-11-26 15:45:51.604136+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (5, 'admin', '0002_logentry_remove_auto_add', '2018-11-26 15:45:51.614424+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (6, 'admin', '0003_logentry_add_action_flag_choices', '2018-11-26 15:45:51.625778+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (7, 'contenttypes', '0002_remove_content_type_name', '2018-11-26 15:45:51.647429+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (8, 'auth', '0002_alter_permission_name_max_length', '2018-11-26 15:45:51.656208+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (9, 'auth', '0003_alter_user_email_max_length', '2018-11-26 15:45:51.670576+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (10, 'auth', '0004_alter_user_username_opts', '2018-11-26 15:45:51.683979+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (11, 'auth', '0005_alter_user_last_login_null', '2018-11-26 15:45:51.697653+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (12, 'auth', '0006_require_contenttypes_0002', '2018-11-26 15:45:51.701093+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (13, 'auth', '0007_alter_validators_add_error_messages', '2018-11-26 15:45:51.714895+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (14, 'auth', '0008_alter_user_username_max_length', '2018-11-26 15:45:51.728984+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (15, 'auth', '0009_alter_user_last_name_max_length', '2018-11-26 15:45:51.7415+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (16, 'django_celery_beat', '0001_initial', '2018-11-26 15:45:51.766358+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (17, 'django_celery_beat', '0002_auto_20161118_0346', '2018-11-26 15:45:51.787418+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (18, 'django_celery_beat', '0003_auto_20161209_0049', '2018-11-26 15:45:51.797503+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (19, 'django_celery_beat', '0004_auto_20170221_0000', '2018-11-26 15:45:51.803083+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (20, 'django_celery_beat', '0005_add_solarschedule_events_choices', '2018-11-26 15:45:51.856984+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (21, 'django_celery_beat', '0006_auto_20180210_1226', '2018-11-26 15:45:51.859402+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (22, 'django_celery_beat', '0006_auto_20180322_0932', '2018-11-26 15:45:51.861571+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (23, 'django_celery_beat', '0007_auto_20180521_0826', '2018-11-26 15:45:51.863476+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (24, 'django_celery_beat', '0008_auto_20180914_1922', '2018-11-26 15:45:51.865298+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (25, 'django_celery_beat', '0006_periodictask_priority', '2018-11-26 15:45:51.873079+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (26, 'django_twilio', '0001_initial', '2018-11-26 15:45:51.89176+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (27, 'schedule', '0001_initial', '2018-11-26 15:45:51.982155+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (28, 'schedule', '0002_event_color_event', '2018-11-26 15:45:51.999265+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (29, 'schedule', '0003_auto_20160715_0028', '2018-11-26 15:45:52.074564+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (30, 'schedule', '0006_update_text_fields_empty_string', '2018-11-26 15:45:52.099369+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (31, 'schedule', '0004_text_fields_not_null', '2018-11-26 15:45:52.216259+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (32, 'schedule', '0005_verbose_name_plural_for_calendar', '2018-11-26 15:45:52.22168+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (33, 'schedule', '0007_merge_text_fields', '2018-11-26 15:45:52.224221+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (34, 'schedule', '0008_gfk_index', '2018-11-26 15:45:52.261259+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (35, 'schedule', '0008_calendar_slug_unique', '2018-11-26 15:45:52.284912+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (36, 'schedule', '0009_merge_20180108_2303', '2018-11-26 15:45:52.287957+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (37, 'schedule', '0010_events_set_missing_calendar', '2018-11-26 15:45:52.308071+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (38, 'schedule', '0011_event_calendar_not_null', '2018-11-26 15:45:52.328782+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (39, 'schedules', '0001_initial', '2018-11-26 15:45:52.360316+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (40, 'services', '0001_initial', '2018-11-26 15:45:52.415879+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (41, 'incidents', '0001_initial', '2018-11-26 15:45:52.429748+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (42, 'incidents', '0002_auto_20181122_1103', '2018-11-26 15:45:52.47447+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (43, 'events', '0001_initial', '2018-11-26 15:45:52.502813+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (44, 'notification', '0001_initial', '2018-11-26 15:45:52.551835+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (45, 'policies', '0001_initial', '2018-11-26 15:45:52.58676+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (46, 'sessions', '0001_initial', '2018-11-26 15:45:52.596207+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (47, 'django_celery_beat', '0005_add_solarschedule_events_choices_squashed_0009_merge_20181012_1416', '2018-11-26 15:45:52.601528+00');


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: openduty
--

INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('wi5hq96qyybnfscbmeoltloladamccci', 'MTcwMWYwYWMzNDJlMmVjNzI1OTJmMjhmNDUxMmNjOGNjNjFkNTZiNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiYjlkMTUxOTc0OWQ5YjJhZTNjMWU2ZTE0MDM5YWY0NzdkZjA0YmVkIn0=', '2018-12-10 15:48:24.842362+00');


--
-- Data for Name: django_twilio_caller; Type: TABLE DATA; Schema: public; Owner: openduty
--

INSERT INTO public.django_twilio_caller (id, blacklisted, phone_number) VALUES (1, false, '+41764744645');
INSERT INTO public.django_twilio_caller (id, blacklisted, phone_number) VALUES (2, false, '+40764744645');


--
-- Data for Name: django_twilio_credential; Type: TABLE DATA; Schema: public; Owner: openduty
--

INSERT INTO public.django_twilio_credential (id, name, account_sid, auth_token, user_id) VALUES (1, 'demo', 'qwertyuiop', 'qwertyuiop', 1);
INSERT INTO public.django_twilio_credential (id, name, account_sid, auth_token, user_id) VALUES (2, 'demo2', 'qwertyuiop', 'qwertyuiop', 2);


--
-- Data for Name: schedules_schedulepolicy; Type: TABLE DATA; Schema: public; Owner: openduty
--

INSERT INTO public.schedules_schedulepolicy (id, name, repeat_times) VALUES (1, 'Demo Schedule Policy 1', 3);
INSERT INTO public.schedules_schedulepolicy (id, name, repeat_times) VALUES (3, 'Demo Schedule Policy  3', 3);
INSERT INTO public.schedules_schedulepolicy (id, name, repeat_times) VALUES (2, 'Demo Schedule Policy 2', 2);


--
-- Data for Name: services_service; Type: TABLE DATA; Schema: public; Owner: openduty
--

INSERT INTO public.services_service (name, id, retry, escalate_after, notifications_disabled, send_resolve_enabled, policy_id) VALUES ('Demo Service key 2', 'ebc956ad-5f0f-4385-8781-9290e4e06902', 2, -1, true, false, 2);
INSERT INTO public.services_service (name, id, retry, escalate_after, notifications_disabled, send_resolve_enabled, policy_id) VALUES ('Demo Service key 3', '2b1e704d-616d-48a6-bfbf-a73382c69deb', 3, 4, false, true, 3);
INSERT INTO public.services_service (name, id, retry, escalate_after, notifications_disabled, send_resolve_enabled, policy_id) VALUES ('Demo Service 2', '7bece19f-057e-4db8-b6a4-5275b6c916d9', 3, 3, false, true, 2);
INSERT INTO public.services_service (name, id, retry, escalate_after, notifications_disabled, send_resolve_enabled, policy_id) VALUES ('Demo Service 1', '1a32b4c9-6ce3-4c0f-a734-046b4c8bdf6f', 3, 1, false, true, 1);
INSERT INTO public.services_service (name, id, retry, escalate_after, notifications_disabled, send_resolve_enabled, policy_id) VALUES ('Demo Service key 1', 'acaede8f-1f05-4d9b-a9e2-747d4140eabf', 3, 2, false, true, 2);


--
-- Data for Name: incidents_incident; Type: TABLE DATA; Schema: public; Owner: openduty
--

INSERT INTO public.incidents_incident (id, incident_key, event_type, description, details, occurred_at, service_key_id, service_to_escalate_to_id) VALUES (1, 'qwerty1', 'acknowledge', 'Demo Description Service 1', 'Demo Details Service 1', '2018-11-26 15:54:39+00', 'acaede8f-1f05-4d9b-a9e2-747d4140eabf', '1a32b4c9-6ce3-4c0f-a734-046b4c8bdf6f');


--
-- Data for Name: events_eventlog; Type: TABLE DATA; Schema: public; Owner: openduty
--

INSERT INTO public.events_eventlog (id, action, data, occurred_at, incident_key_id, service_key_id, user_id) VALUES (1, 'log', 'Some demo data about this Event', '2018-11-26 15:55:40+00', 1, '7bece19f-057e-4db8-b6a4-5275b6c916d9', 1);
INSERT INTO public.events_eventlog (id, action, data, occurred_at, incident_key_id, service_key_id, user_id) VALUES (2, 'notified', 'The password is too similar to the email address.
This password is too short. It must contain at least 8 characters.', '2018-11-26 21:53:09+00', 1, 'ebc956ad-5f0f-4385-8781-9290e4e06902', 2);
INSERT INTO public.events_eventlog (id, action, data, occurred_at, incident_key_id, service_key_id, user_id) VALUES (3, 'resolve', 'The password is too similar to the email address.
This password is too short. It must contain at least 8 characters.', '2018-11-26 21:53:30+00', 1, '7bece19f-057e-4db8-b6a4-5275b6c916d9', 1);
INSERT INTO public.events_eventlog (id, action, data, occurred_at, incident_key_id, service_key_id, user_id) VALUES (4, 'unsilence_incident', 'The password is too similar to the email address.', '2018-11-26 22:53:50+00', 1, '7bece19f-057e-4db8-b6a4-5275b6c916d9', 2);
INSERT INTO public.events_eventlog (id, action, data, occurred_at, incident_key_id, service_key_id, user_id) VALUES (5, 'unsilence_incident', 'GRANT ALL ON SCHEMA public TO PUBLIC;', '2018-11-25 06:00:00+00', 1, 'acaede8f-1f05-4d9b-a9e2-747d4140eabf', 1);


--
-- Data for Name: incidents_incidentsilenced; Type: TABLE DATA; Schema: public; Owner: openduty
--



--
-- Data for Name: openduty_schedulednotification; Type: TABLE DATA; Schema: public; Owner: openduty
--



--
-- Data for Name: openduty_usernotificationmethod; Type: TABLE DATA; Schema: public; Owner: openduty
--



--
-- Data for Name: policies_schedulepolicy; Type: TABLE DATA; Schema: public; Owner: openduty
--

INSERT INTO public.policies_schedulepolicy (id, name, repeat_times) VALUES (1, 'Policy 1', 3);
INSERT INTO public.policies_schedulepolicy (id, name, repeat_times) VALUES (2, 'Policy 2', 5);
INSERT INTO public.policies_schedulepolicy (id, name, repeat_times) VALUES (3, 'Policy 3', 2);


--
-- Data for Name: schedule_calendar; Type: TABLE DATA; Schema: public; Owner: openduty
--

INSERT INTO public.schedule_calendar (id, name, slug) VALUES (1, 'Demo', 'demo-1');
INSERT INTO public.schedule_calendar (id, name, slug) VALUES (2, 'Calendar 2', 'calendar-2');


--
-- Data for Name: policies_schedulepolicyrule; Type: TABLE DATA; Schema: public; Owner: openduty
--

INSERT INTO public.policies_schedulepolicyrule (id, "position", escalate_after, group_id_id, schedule_id, schedule_policy_id, user_id_id) VALUES (1, 1, 0, NULL, 1, 1, NULL);
INSERT INTO public.policies_schedulepolicyrule (id, "position", escalate_after, group_id_id, schedule_id, schedule_policy_id, user_id_id) VALUES (2, 1, 0, NULL, NULL, 2, 1);
INSERT INTO public.policies_schedulepolicyrule (id, "position", escalate_after, group_id_id, schedule_id, schedule_policy_id, user_id_id) VALUES (3, 1, 0, NULL, 1, 3, NULL);


--
-- Data for Name: schedule_calendarrelation; Type: TABLE DATA; Schema: public; Owner: openduty
--



--
-- Data for Name: schedule_rule; Type: TABLE DATA; Schema: public; Owner: openduty
--

INSERT INTO public.schedule_rule (id, name, description, frequency, params) VALUES (1, 'Schedule Rule 1', 'Demo content description about Schedule Rule 1', 'HOURLY', 'Demo content description about Schedule Rule 1');
INSERT INTO public.schedule_rule (id, name, description, frequency, params) VALUES (2, 'Rule 2', 'description rule 2', 'MINUTELY', 'a = 2');


--
-- Data for Name: schedule_event; Type: TABLE DATA; Schema: public; Owner: openduty
--

INSERT INTO public.schedule_event (id, start, "end", title, description, created_on, updated_on, end_recurring_period, calendar_id, creator_id, rule_id, color_event) VALUES (1, '2018-11-26 20:27:28+00', '2018-11-27 20:27:35+00', 'Event 1', 'Demo content description about event 1', '2018-11-26 20:28:24.843332+00', '2018-11-26 20:28:24.843348+00', '2018-11-30 20:28:23+00', 1, 1, 1, '#000000');
INSERT INTO public.schedule_event (id, start, "end", title, description, created_on, updated_on, end_recurring_period, calendar_id, creator_id, rule_id, color_event) VALUES (2, '2018-11-28 00:00:00+00', '2018-12-29 00:00:00+00', 'Event 2', '', '2018-11-26 21:12:02.045208+00', '2018-11-26 21:43:54.401932+00', '2018-12-09 21:11:28+00', 2, 1, 2, '#000000');
INSERT INTO public.schedule_event (id, start, "end", title, description, created_on, updated_on, end_recurring_period, calendar_id, creator_id, rule_id, color_event) VALUES (3, '2018-11-27 00:00:00+00', '2018-11-28 00:00:00+00', 'demo, demo', 'wqertyu', '2018-11-26 21:33:54.074665+00', '2018-11-26 21:44:16.496715+00', '2018-11-30 00:00:00+00', 2, 1, 2, '#000000');


--
-- Data for Name: schedule_eventrelation; Type: TABLE DATA; Schema: public; Owner: openduty
--



--
-- Data for Name: schedule_occurrence; Type: TABLE DATA; Schema: public; Owner: openduty
--



--
-- Data for Name: schedules_schedulepolicyrule; Type: TABLE DATA; Schema: public; Owner: openduty
--



--
-- Data for Name: services_servicesilenced; Type: TABLE DATA; Schema: public; Owner: openduty
--



--
-- Data for Name: services_servicetokens; Type: TABLE DATA; Schema: public; Owner: openduty
--

INSERT INTO public.services_servicetokens (id, name, service_id_id, token_id_id) VALUES (1, '', '1a32b4c9-6ce3-4c0f-a734-046b4c8bdf6f', '4bb275bcb4ca991da2dff78e548278c890ed6f96');
INSERT INTO public.services_servicetokens (id, name, service_id_id, token_id_id) VALUES (2, '', 'acaede8f-1f05-4d9b-a9e2-747d4140eabf', 'cda95a1a396ddf028d040355a534e746e980ce6d');
INSERT INTO public.services_servicetokens (id, name, service_id_id, token_id_id) VALUES (3, '', 'acaede8f-1f05-4d9b-a9e2-747d4140eabf', '0aa8fe734605e984500df39f756fc925af1b46e4');


--
-- Name: accounts_userprofile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.accounts_userprofile_id_seq', 2, true);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, true);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 132, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 2, true);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 2, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 38, true);


--
-- Name: django_celery_beat_crontabschedule_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.django_celery_beat_crontabschedule_id_seq', 1, false);


--
-- Name: django_celery_beat_intervalschedule_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.django_celery_beat_intervalschedule_id_seq', 1, false);


--
-- Name: django_celery_beat_periodictask_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.django_celery_beat_periodictask_id_seq', 1, false);


--
-- Name: django_celery_beat_solarschedule_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.django_celery_beat_solarschedule_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 33, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 47, true);


--
-- Name: django_twilio_caller_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.django_twilio_caller_id_seq', 2, true);


--
-- Name: django_twilio_credential_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.django_twilio_credential_id_seq', 2, true);


--
-- Name: events_eventlog_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.events_eventlog_id_seq', 5, true);


--
-- Name: incidents_incident_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.incidents_incident_id_seq', 1, true);


--
-- Name: incidents_incidentsilenced_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.incidents_incidentsilenced_id_seq', 1, false);


--
-- Name: openduty_schedulednotification_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.openduty_schedulednotification_id_seq', 1, false);


--
-- Name: openduty_usernotificationmethod_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.openduty_usernotificationmethod_id_seq', 1, false);


--
-- Name: policies_schedulepolicy_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.policies_schedulepolicy_id_seq', 3, true);


--
-- Name: policies_schedulepolicyrule_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.policies_schedulepolicyrule_id_seq', 3, true);


--
-- Name: schedule_calendar_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.schedule_calendar_id_seq', 2, true);


--
-- Name: schedule_calendarrelation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.schedule_calendarrelation_id_seq', 1, false);


--
-- Name: schedule_event_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.schedule_event_id_seq', 3, true);


--
-- Name: schedule_eventrelation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.schedule_eventrelation_id_seq', 1, false);


--
-- Name: schedule_occurrence_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.schedule_occurrence_id_seq', 1, false);


--
-- Name: schedule_rule_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.schedule_rule_id_seq', 2, true);


--
-- Name: schedules_schedulepolicy_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.schedules_schedulepolicy_id_seq', 3, true);


--
-- Name: schedules_schedulepolicyrule_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.schedules_schedulepolicyrule_id_seq', 1, false);


--
-- Name: services_servicesilenced_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.services_servicesilenced_id_seq', 1, false);


--
-- Name: services_servicetokens_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.services_servicetokens_id_seq', 3, true);


--
-- PostgreSQL database dump complete
--

