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
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: accounts_token; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.accounts_token (
    key character varying(40) NOT NULL,
    created timestamp with time zone NOT NULL
);


ALTER TABLE public.accounts_token OWNER TO openduty;

--
-- Name: accounts_userprofile; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.accounts_userprofile (
    id integer NOT NULL,
    phone_number character varying(50) NOT NULL,
    pushover_user_key character varying(50) NOT NULL,
    pushover_app_key character varying(50) NOT NULL,
    slack_room_name character varying(50) NOT NULL,
    prowl_api_key character varying(50) NOT NULL,
    prowl_application character varying(256) NOT NULL,
    prowl_url character varying(512) NOT NULL,
    rocket_webhook_url character varying(512) NOT NULL,
    hipchat_room_name character varying(100) NOT NULL,
    hipchat_room_url character varying(100) NOT NULL,
    send_resolve_enabled boolean NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.accounts_userprofile OWNER TO openduty;

--
-- Name: accounts_userprofile_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.accounts_userprofile_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.accounts_userprofile_id_seq OWNER TO openduty;

--
-- Name: accounts_userprofile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.accounts_userprofile_id_seq OWNED BY public.accounts_userprofile.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO openduty;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO openduty;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO openduty;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO openduty;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO openduty;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO openduty;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO openduty;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO openduty;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO openduty;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO openduty;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO openduty;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO openduty;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO openduty;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO openduty;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_celery_beat_crontabschedule; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.django_celery_beat_crontabschedule (
    id integer NOT NULL,
    minute character varying(240) NOT NULL,
    hour character varying(96) NOT NULL,
    day_of_week character varying(64) NOT NULL,
    day_of_month character varying(124) NOT NULL,
    month_of_year character varying(64) NOT NULL,
    timezone character varying(63) NOT NULL
);


ALTER TABLE public.django_celery_beat_crontabschedule OWNER TO openduty;

--
-- Name: django_celery_beat_crontabschedule_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.django_celery_beat_crontabschedule_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_celery_beat_crontabschedule_id_seq OWNER TO openduty;

--
-- Name: django_celery_beat_crontabschedule_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.django_celery_beat_crontabschedule_id_seq OWNED BY public.django_celery_beat_crontabschedule.id;


--
-- Name: django_celery_beat_intervalschedule; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.django_celery_beat_intervalschedule (
    id integer NOT NULL,
    every integer NOT NULL,
    period character varying(24) NOT NULL
);


ALTER TABLE public.django_celery_beat_intervalschedule OWNER TO openduty;

--
-- Name: django_celery_beat_intervalschedule_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.django_celery_beat_intervalschedule_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_celery_beat_intervalschedule_id_seq OWNER TO openduty;

--
-- Name: django_celery_beat_intervalschedule_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.django_celery_beat_intervalschedule_id_seq OWNED BY public.django_celery_beat_intervalschedule.id;


--
-- Name: django_celery_beat_periodictask; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.django_celery_beat_periodictask (
    id integer NOT NULL,
    name character varying(200) NOT NULL,
    task character varying(200) NOT NULL,
    args text NOT NULL,
    kwargs text NOT NULL,
    queue character varying(200),
    exchange character varying(200),
    routing_key character varying(200),
    expires timestamp with time zone,
    enabled boolean NOT NULL,
    last_run_at timestamp with time zone,
    total_run_count integer NOT NULL,
    date_changed timestamp with time zone NOT NULL,
    description text NOT NULL,
    crontab_id integer,
    interval_id integer,
    solar_id integer,
    one_off boolean NOT NULL,
    start_time timestamp with time zone,
    priority integer,
    CONSTRAINT django_celery_beat_periodictask_priority_check CHECK ((priority >= 0)),
    CONSTRAINT django_celery_beat_periodictask_total_run_count_check CHECK ((total_run_count >= 0))
);


ALTER TABLE public.django_celery_beat_periodictask OWNER TO openduty;

--
-- Name: django_celery_beat_periodictask_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.django_celery_beat_periodictask_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_celery_beat_periodictask_id_seq OWNER TO openduty;

--
-- Name: django_celery_beat_periodictask_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.django_celery_beat_periodictask_id_seq OWNED BY public.django_celery_beat_periodictask.id;


--
-- Name: django_celery_beat_periodictasks; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.django_celery_beat_periodictasks (
    ident smallint NOT NULL,
    last_update timestamp with time zone NOT NULL
);


ALTER TABLE public.django_celery_beat_periodictasks OWNER TO openduty;

--
-- Name: django_celery_beat_solarschedule; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.django_celery_beat_solarschedule (
    id integer NOT NULL,
    event character varying(24) NOT NULL,
    latitude numeric(9,6) NOT NULL,
    longitude numeric(9,6) NOT NULL
);


ALTER TABLE public.django_celery_beat_solarschedule OWNER TO openduty;

--
-- Name: django_celery_beat_solarschedule_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.django_celery_beat_solarschedule_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_celery_beat_solarschedule_id_seq OWNER TO openduty;

--
-- Name: django_celery_beat_solarschedule_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.django_celery_beat_solarschedule_id_seq OWNED BY public.django_celery_beat_solarschedule.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO openduty;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO openduty;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO openduty;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO openduty;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO openduty;

--
-- Name: django_twilio_caller; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.django_twilio_caller (
    id integer NOT NULL,
    blacklisted boolean NOT NULL,
    phone_number character varying(128) NOT NULL
);


ALTER TABLE public.django_twilio_caller OWNER TO openduty;

--
-- Name: django_twilio_caller_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.django_twilio_caller_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_twilio_caller_id_seq OWNER TO openduty;

--
-- Name: django_twilio_caller_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.django_twilio_caller_id_seq OWNED BY public.django_twilio_caller.id;


--
-- Name: django_twilio_credential; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.django_twilio_credential (
    id integer NOT NULL,
    name character varying(30) NOT NULL,
    account_sid character varying(34) NOT NULL,
    auth_token character varying(32) NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.django_twilio_credential OWNER TO openduty;

--
-- Name: django_twilio_credential_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.django_twilio_credential_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_twilio_credential_id_seq OWNER TO openduty;

--
-- Name: django_twilio_credential_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.django_twilio_credential_id_seq OWNED BY public.django_twilio_credential.id;


--
-- Name: events_eventlog; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.events_eventlog (
    id integer NOT NULL,
    action character varying(100) NOT NULL,
    data text NOT NULL,
    occurred_at timestamp with time zone NOT NULL,
    incident_key_id integer,
    service_key_id uuid NOT NULL,
    user_id integer
);


ALTER TABLE public.events_eventlog OWNER TO openduty;

--
-- Name: events_eventlog_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.events_eventlog_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.events_eventlog_id_seq OWNER TO openduty;

--
-- Name: events_eventlog_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.events_eventlog_id_seq OWNED BY public.events_eventlog.id;


--
-- Name: incidents_incident; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.incidents_incident (
    id integer NOT NULL,
    incident_key character varying(200) NOT NULL,
    event_type character varying(15) NOT NULL,
    description character varying(200) NOT NULL,
    details text NOT NULL,
    occurred_at timestamp with time zone NOT NULL,
    service_key_id uuid NOT NULL,
    service_to_escalate_to_id uuid
);


ALTER TABLE public.incidents_incident OWNER TO openduty;

--
-- Name: incidents_incident_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.incidents_incident_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.incidents_incident_id_seq OWNER TO openduty;

--
-- Name: incidents_incident_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.incidents_incident_id_seq OWNED BY public.incidents_incident.id;


--
-- Name: incidents_incidentsilenced; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.incidents_incidentsilenced (
    id integer NOT NULL,
    silenced boolean NOT NULL,
    silenced_until timestamp with time zone NOT NULL,
    incident_id integer NOT NULL
);


ALTER TABLE public.incidents_incidentsilenced OWNER TO openduty;

--
-- Name: incidents_incidentsilenced_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.incidents_incidentsilenced_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.incidents_incidentsilenced_id_seq OWNER TO openduty;

--
-- Name: incidents_incidentsilenced_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.incidents_incidentsilenced_id_seq OWNED BY public.incidents_incidentsilenced.id;


--
-- Name: openduty_schedulednotification; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.openduty_schedulednotification (
    id integer NOT NULL,
    notifier character varying(30) NOT NULL,
    message character varying(500) NOT NULL,
    send_at timestamp with time zone NOT NULL,
    incident_id integer,
    user_to_notify_id integer NOT NULL
);


ALTER TABLE public.openduty_schedulednotification OWNER TO openduty;

--
-- Name: openduty_schedulednotification_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.openduty_schedulednotification_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.openduty_schedulednotification_id_seq OWNER TO openduty;

--
-- Name: openduty_schedulednotification_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.openduty_schedulednotification_id_seq OWNED BY public.openduty_schedulednotification.id;


--
-- Name: openduty_usernotificationmethod; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.openduty_usernotificationmethod (
    id integer NOT NULL,
    "position" integer NOT NULL,
    method character varying(50) NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.openduty_usernotificationmethod OWNER TO openduty;

--
-- Name: openduty_usernotificationmethod_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.openduty_usernotificationmethod_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.openduty_usernotificationmethod_id_seq OWNER TO openduty;

--
-- Name: openduty_usernotificationmethod_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.openduty_usernotificationmethod_id_seq OWNED BY public.openduty_usernotificationmethod.id;


--
-- Name: policies_schedulepolicy; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.policies_schedulepolicy (
    id integer NOT NULL,
    name character varying(80) NOT NULL,
    repeat_times integer NOT NULL
);


ALTER TABLE public.policies_schedulepolicy OWNER TO openduty;

--
-- Name: policies_schedulepolicy_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.policies_schedulepolicy_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.policies_schedulepolicy_id_seq OWNER TO openduty;

--
-- Name: policies_schedulepolicy_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.policies_schedulepolicy_id_seq OWNED BY public.policies_schedulepolicy.id;


--
-- Name: policies_schedulepolicyrule; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.policies_schedulepolicyrule (
    id integer NOT NULL,
    "position" integer NOT NULL,
    escalate_after integer NOT NULL,
    group_id_id integer,
    schedule_id integer,
    schedule_policy_id integer NOT NULL,
    user_id_id integer
);


ALTER TABLE public.policies_schedulepolicyrule OWNER TO openduty;

--
-- Name: policies_schedulepolicyrule_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.policies_schedulepolicyrule_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.policies_schedulepolicyrule_id_seq OWNER TO openduty;

--
-- Name: policies_schedulepolicyrule_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.policies_schedulepolicyrule_id_seq OWNED BY public.policies_schedulepolicyrule.id;


--
-- Name: schedule_calendar; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.schedule_calendar (
    id integer NOT NULL,
    name character varying(200) NOT NULL,
    slug character varying(200) NOT NULL
);


ALTER TABLE public.schedule_calendar OWNER TO openduty;

--
-- Name: schedule_calendar_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.schedule_calendar_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.schedule_calendar_id_seq OWNER TO openduty;

--
-- Name: schedule_calendar_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.schedule_calendar_id_seq OWNED BY public.schedule_calendar.id;


--
-- Name: schedule_calendarrelation; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.schedule_calendarrelation (
    id integer NOT NULL,
    object_id integer NOT NULL,
    distinction character varying(20) NOT NULL,
    inheritable boolean NOT NULL,
    calendar_id integer NOT NULL,
    content_type_id integer NOT NULL
);


ALTER TABLE public.schedule_calendarrelation OWNER TO openduty;

--
-- Name: schedule_calendarrelation_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.schedule_calendarrelation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.schedule_calendarrelation_id_seq OWNER TO openduty;

--
-- Name: schedule_calendarrelation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.schedule_calendarrelation_id_seq OWNED BY public.schedule_calendarrelation.id;


--
-- Name: schedule_event; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.schedule_event (
    id integer NOT NULL,
    start timestamp with time zone NOT NULL,
    "end" timestamp with time zone NOT NULL,
    title character varying(255) NOT NULL,
    description text NOT NULL,
    created_on timestamp with time zone NOT NULL,
    updated_on timestamp with time zone NOT NULL,
    end_recurring_period timestamp with time zone,
    calendar_id integer NOT NULL,
    creator_id integer,
    rule_id integer,
    color_event character varying(10) NOT NULL
);


ALTER TABLE public.schedule_event OWNER TO openduty;

--
-- Name: schedule_event_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.schedule_event_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.schedule_event_id_seq OWNER TO openduty;

--
-- Name: schedule_event_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.schedule_event_id_seq OWNED BY public.schedule_event.id;


--
-- Name: schedule_eventrelation; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.schedule_eventrelation (
    id integer NOT NULL,
    object_id integer NOT NULL,
    distinction character varying(20) NOT NULL,
    content_type_id integer NOT NULL,
    event_id integer NOT NULL
);


ALTER TABLE public.schedule_eventrelation OWNER TO openduty;

--
-- Name: schedule_eventrelation_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.schedule_eventrelation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.schedule_eventrelation_id_seq OWNER TO openduty;

--
-- Name: schedule_eventrelation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.schedule_eventrelation_id_seq OWNED BY public.schedule_eventrelation.id;


--
-- Name: schedule_occurrence; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.schedule_occurrence (
    id integer NOT NULL,
    title character varying(255) NOT NULL,
    description text NOT NULL,
    start timestamp with time zone NOT NULL,
    "end" timestamp with time zone NOT NULL,
    cancelled boolean NOT NULL,
    original_start timestamp with time zone NOT NULL,
    original_end timestamp with time zone NOT NULL,
    created_on timestamp with time zone NOT NULL,
    updated_on timestamp with time zone NOT NULL,
    event_id integer NOT NULL
);


ALTER TABLE public.schedule_occurrence OWNER TO openduty;

--
-- Name: schedule_occurrence_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.schedule_occurrence_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.schedule_occurrence_id_seq OWNER TO openduty;

--
-- Name: schedule_occurrence_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.schedule_occurrence_id_seq OWNED BY public.schedule_occurrence.id;


--
-- Name: schedule_rule; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.schedule_rule (
    id integer NOT NULL,
    name character varying(32) NOT NULL,
    description text NOT NULL,
    frequency character varying(10) NOT NULL,
    params text NOT NULL
);


ALTER TABLE public.schedule_rule OWNER TO openduty;

--
-- Name: schedule_rule_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.schedule_rule_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.schedule_rule_id_seq OWNER TO openduty;

--
-- Name: schedule_rule_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.schedule_rule_id_seq OWNED BY public.schedule_rule.id;


--
-- Name: schedules_schedulepolicy; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.schedules_schedulepolicy (
    id integer NOT NULL,
    name character varying(80) NOT NULL,
    repeat_times integer NOT NULL
);


ALTER TABLE public.schedules_schedulepolicy OWNER TO openduty;

--
-- Name: schedules_schedulepolicy_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.schedules_schedulepolicy_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.schedules_schedulepolicy_id_seq OWNER TO openduty;

--
-- Name: schedules_schedulepolicy_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.schedules_schedulepolicy_id_seq OWNED BY public.schedules_schedulepolicy.id;


--
-- Name: schedules_schedulepolicyrule; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.schedules_schedulepolicyrule (
    id integer NOT NULL,
    "position" integer NOT NULL,
    escalate_after integer NOT NULL,
    group_id_id integer,
    schedule_id integer,
    schedule_policy_id integer NOT NULL,
    user_id_id integer
);


ALTER TABLE public.schedules_schedulepolicyrule OWNER TO openduty;

--
-- Name: schedules_schedulepolicyrule_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.schedules_schedulepolicyrule_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.schedules_schedulepolicyrule_id_seq OWNER TO openduty;

--
-- Name: schedules_schedulepolicyrule_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.schedules_schedulepolicyrule_id_seq OWNED BY public.schedules_schedulepolicyrule.id;


--
-- Name: services_service; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.services_service (
    name character varying(80) NOT NULL,
    id uuid NOT NULL,
    retry integer,
    escalate_after integer,
    notifications_disabled boolean NOT NULL,
    send_resolve_enabled boolean NOT NULL,
    policy_id integer
);


ALTER TABLE public.services_service OWNER TO openduty;

--
-- Name: services_servicesilenced; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.services_servicesilenced (
    id integer NOT NULL,
    silenced boolean NOT NULL,
    silenced_until timestamp with time zone NOT NULL,
    service_id uuid NOT NULL
);


ALTER TABLE public.services_servicesilenced OWNER TO openduty;

--
-- Name: services_servicesilenced_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.services_servicesilenced_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.services_servicesilenced_id_seq OWNER TO openduty;

--
-- Name: services_servicesilenced_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.services_servicesilenced_id_seq OWNED BY public.services_servicesilenced.id;


--
-- Name: services_servicetokens; Type: TABLE; Schema: public; Owner: openduty
--

CREATE TABLE public.services_servicetokens (
    id integer NOT NULL,
    name character varying(80) NOT NULL,
    service_id_id uuid NOT NULL,
    token_id_id character varying(40) NOT NULL
);


ALTER TABLE public.services_servicetokens OWNER TO openduty;

--
-- Name: services_servicetokens_id_seq; Type: SEQUENCE; Schema: public; Owner: openduty
--

CREATE SEQUENCE public.services_servicetokens_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.services_servicetokens_id_seq OWNER TO openduty;

--
-- Name: services_servicetokens_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: openduty
--

ALTER SEQUENCE public.services_servicetokens_id_seq OWNED BY public.services_servicetokens.id;


--
-- Name: accounts_userprofile id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.accounts_userprofile ALTER COLUMN id SET DEFAULT nextval('public.accounts_userprofile_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_celery_beat_crontabschedule id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_celery_beat_crontabschedule ALTER COLUMN id SET DEFAULT nextval('public.django_celery_beat_crontabschedule_id_seq'::regclass);


--
-- Name: django_celery_beat_intervalschedule id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_celery_beat_intervalschedule ALTER COLUMN id SET DEFAULT nextval('public.django_celery_beat_intervalschedule_id_seq'::regclass);


--
-- Name: django_celery_beat_periodictask id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_celery_beat_periodictask ALTER COLUMN id SET DEFAULT nextval('public.django_celery_beat_periodictask_id_seq'::regclass);


--
-- Name: django_celery_beat_solarschedule id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_celery_beat_solarschedule ALTER COLUMN id SET DEFAULT nextval('public.django_celery_beat_solarschedule_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: django_twilio_caller id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_twilio_caller ALTER COLUMN id SET DEFAULT nextval('public.django_twilio_caller_id_seq'::regclass);


--
-- Name: django_twilio_credential id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_twilio_credential ALTER COLUMN id SET DEFAULT nextval('public.django_twilio_credential_id_seq'::regclass);


--
-- Name: events_eventlog id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.events_eventlog ALTER COLUMN id SET DEFAULT nextval('public.events_eventlog_id_seq'::regclass);


--
-- Name: incidents_incident id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.incidents_incident ALTER COLUMN id SET DEFAULT nextval('public.incidents_incident_id_seq'::regclass);


--
-- Name: incidents_incidentsilenced id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.incidents_incidentsilenced ALTER COLUMN id SET DEFAULT nextval('public.incidents_incidentsilenced_id_seq'::regclass);


--
-- Name: openduty_schedulednotification id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.openduty_schedulednotification ALTER COLUMN id SET DEFAULT nextval('public.openduty_schedulednotification_id_seq'::regclass);


--
-- Name: openduty_usernotificationmethod id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.openduty_usernotificationmethod ALTER COLUMN id SET DEFAULT nextval('public.openduty_usernotificationmethod_id_seq'::regclass);


--
-- Name: policies_schedulepolicy id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.policies_schedulepolicy ALTER COLUMN id SET DEFAULT nextval('public.policies_schedulepolicy_id_seq'::regclass);


--
-- Name: policies_schedulepolicyrule id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.policies_schedulepolicyrule ALTER COLUMN id SET DEFAULT nextval('public.policies_schedulepolicyrule_id_seq'::regclass);


--
-- Name: schedule_calendar id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedule_calendar ALTER COLUMN id SET DEFAULT nextval('public.schedule_calendar_id_seq'::regclass);


--
-- Name: schedule_calendarrelation id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedule_calendarrelation ALTER COLUMN id SET DEFAULT nextval('public.schedule_calendarrelation_id_seq'::regclass);


--
-- Name: schedule_event id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedule_event ALTER COLUMN id SET DEFAULT nextval('public.schedule_event_id_seq'::regclass);


--
-- Name: schedule_eventrelation id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedule_eventrelation ALTER COLUMN id SET DEFAULT nextval('public.schedule_eventrelation_id_seq'::regclass);


--
-- Name: schedule_occurrence id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedule_occurrence ALTER COLUMN id SET DEFAULT nextval('public.schedule_occurrence_id_seq'::regclass);


--
-- Name: schedule_rule id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedule_rule ALTER COLUMN id SET DEFAULT nextval('public.schedule_rule_id_seq'::regclass);


--
-- Name: schedules_schedulepolicy id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedules_schedulepolicy ALTER COLUMN id SET DEFAULT nextval('public.schedules_schedulepolicy_id_seq'::regclass);


--
-- Name: schedules_schedulepolicyrule id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedules_schedulepolicyrule ALTER COLUMN id SET DEFAULT nextval('public.schedules_schedulepolicyrule_id_seq'::regclass);


--
-- Name: services_servicesilenced id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.services_servicesilenced ALTER COLUMN id SET DEFAULT nextval('public.services_servicesilenced_id_seq'::regclass);


--
-- Name: services_servicetokens id; Type: DEFAULT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.services_servicetokens ALTER COLUMN id SET DEFAULT nextval('public.services_servicetokens_id_seq'::regclass);


--
-- Data for Name: accounts_token; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.accounts_token (key, created) FROM stdin;
qwertyuiop	2018-11-26 15:49:59.102852+00
4bb275bcb4ca991da2dff78e548278c890ed6f96	2018-11-26 16:18:12.910669+00
cda95a1a396ddf028d040355a534e746e980ce6d	2018-11-26 16:18:28.888884+00
0aa8fe734605e984500df39f756fc925af1b46e4	2018-11-26 16:18:31.396802+00
\.


--
-- Data for Name: accounts_userprofile; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.accounts_userprofile (id, phone_number, pushover_user_key, pushover_app_key, slack_room_name, prowl_api_key, prowl_application, prowl_url, rocket_webhook_url, hipchat_room_name, hipchat_room_url, send_resolve_enabled, user_id) FROM stdin;
1	+41764744645	qwertyuiop	qwertyuiop	qwertyuiop	qwertyuiop	qwertyuiop	qwertyuiop	qwertyuiop	qwertyuiop	qwertyuiop	t	1
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add crontab	7	add_crontabschedule
26	Can change crontab	7	change_crontabschedule
27	Can delete crontab	7	delete_crontabschedule
28	Can view crontab	7	view_crontabschedule
29	Can add interval	8	add_intervalschedule
30	Can change interval	8	change_intervalschedule
31	Can delete interval	8	delete_intervalschedule
32	Can view interval	8	view_intervalschedule
33	Can add periodic task	9	add_periodictask
34	Can change periodic task	9	change_periodictask
35	Can delete periodic task	9	delete_periodictask
36	Can view periodic task	9	view_periodictask
37	Can add periodic tasks	10	add_periodictasks
38	Can change periodic tasks	10	change_periodictasks
39	Can delete periodic tasks	10	delete_periodictasks
40	Can view periodic tasks	10	view_periodictasks
41	Can add solar event	11	add_solarschedule
42	Can change solar event	11	change_solarschedule
43	Can delete solar event	11	delete_solarschedule
44	Can view solar event	11	view_solarschedule
45	Can add caller	12	add_caller
46	Can change caller	12	change_caller
47	Can delete caller	12	delete_caller
48	Can view caller	12	view_caller
49	Can add credential	13	add_credential
50	Can change credential	13	change_credential
51	Can delete credential	13	delete_credential
52	Can view credential	13	view_credential
53	Can add calendar	14	add_calendar
54	Can change calendar	14	change_calendar
55	Can delete calendar	14	delete_calendar
56	Can view calendar	14	view_calendar
57	Can add calendar relation	15	add_calendarrelation
58	Can change calendar relation	15	change_calendarrelation
59	Can delete calendar relation	15	delete_calendarrelation
60	Can view calendar relation	15	view_calendarrelation
61	Can add event	16	add_event
62	Can change event	16	change_event
63	Can delete event	16	delete_event
64	Can view event	16	view_event
65	Can add event relation	17	add_eventrelation
66	Can change event relation	17	change_eventrelation
67	Can delete event relation	17	delete_eventrelation
68	Can view event relation	17	view_eventrelation
69	Can add occurrence	18	add_occurrence
70	Can change occurrence	18	change_occurrence
71	Can delete occurrence	18	delete_occurrence
72	Can view occurrence	18	view_occurrence
73	Can add rule	19	add_rule
74	Can change rule	19	change_rule
75	Can delete rule	19	delete_rule
76	Can view rule	19	view_rule
77	Can add token	20	add_token
78	Can change token	20	change_token
79	Can delete token	20	delete_token
80	Can view token	20	view_token
81	Can add user profile	21	add_userprofile
82	Can change user profile	21	change_userprofile
83	Can delete user profile	21	delete_userprofile
84	Can view user profile	21	view_userprofile
85	Can add eventlog	22	add_eventlog
86	Can change eventlog	22	change_eventlog
87	Can delete eventlog	22	delete_eventlog
88	Can view eventlog	22	view_eventlog
89	Can add incidents	23	add_incident
90	Can change incidents	23	change_incident
91	Can delete incidents	23	delete_incident
92	Can view incidents	23	view_incident
93	Can add incident silenced	24	add_incidentsilenced
94	Can change incident silenced	24	change_incidentsilenced
95	Can delete incident silenced	24	delete_incidentsilenced
96	Can view incident silenced	24	view_incidentsilenced
97	Can add scheduled_notifications	25	add_schedulednotification
98	Can change scheduled_notifications	25	change_schedulednotification
99	Can delete scheduled_notifications	25	delete_schedulednotification
100	Can view scheduled_notifications	25	view_schedulednotification
101	Can add user_notification_method	26	add_usernotificationmethod
102	Can change user_notification_method	26	change_usernotificationmethod
103	Can delete user_notification_method	26	delete_usernotificationmethod
104	Can view user_notification_method	26	view_usernotificationmethod
105	Can add schedule_policy	27	add_schedulepolicy
106	Can change schedule_policy	27	change_schedulepolicy
107	Can delete schedule_policy	27	delete_schedulepolicy
108	Can view schedule_policy	27	view_schedulepolicy
109	Can add schedule_policy_rule	28	add_schedulepolicyrule
110	Can change schedule_policy_rule	28	change_schedulepolicyrule
111	Can delete schedule_policy_rule	28	delete_schedulepolicyrule
112	Can view schedule_policy_rule	28	view_schedulepolicyrule
113	Can add schedule_policy	29	add_schedulepolicy
114	Can change schedule_policy	29	change_schedulepolicy
115	Can delete schedule_policy	29	delete_schedulepolicy
116	Can view schedule_policy	29	view_schedulepolicy
117	Can add schedule_policy_rule	30	add_schedulepolicyrule
118	Can change schedule_policy_rule	30	change_schedulepolicyrule
119	Can delete schedule_policy_rule	30	delete_schedulepolicyrule
120	Can view schedule_policy_rule	30	view_schedulepolicyrule
121	Can add service	31	add_service
122	Can change service	31	change_service
123	Can delete service	31	delete_service
124	Can view service	31	view_service
125	Can add service silenced	32	add_servicesilenced
126	Can change service silenced	32	change_servicesilenced
127	Can delete service silenced	32	delete_servicesilenced
128	Can view service silenced	32	view_servicesilenced
129	Can add service_tokens	33	add_servicetokens
130	Can change service_tokens	33	change_servicetokens
131	Can delete service_tokens	33	delete_servicetokens
132	Can view service_tokens	33	view_servicetokens
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$120000$IvDAiB0mm2xj$Z1v52Zwhfu5tIatYprsC2IS+tIL0Y1UmDSqSkevdLpg=	2018-11-26 15:48:24.839323+00	t	demo			demo@openduty.com	t	t	2018-11-26 15:46:53.569285+00
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2018-11-26 15:49:47.906564+00	1	UserProfile object (1)	1	[{"added": {}}]	21	1
2	2018-11-26 15:49:59.104197+00	qwertyuiop	qwertyuiop	1	[{"added": {}}]	20	1
3	2018-11-26 15:50:15.073161+00	1	+41764744645	1	[{"added": {}}]	12	1
4	2018-11-26 15:50:29.018017+00	1	demo - qwertyuiop	1	[{"added": {}}]	13	1
5	2018-11-26 15:51:29.828802+00	1	Demo Schedule Policy 1	1	[{"added": {}}]	29	1
6	2018-11-26 15:51:41.901184+00	2	Demo Schedule Policy 3	1	[{"added": {}}]	29	1
7	2018-11-26 15:51:52.142217+00	3	Demo Schedule Policy  2	1	[{"added": {}}]	29	1
8	2018-11-26 15:52:11.694744+00	2	Demo Schedule Policy2	2	[{"changed": {"fields": ["name"]}}]	29	1
9	2018-11-26 15:52:19.925731+00	3	Demo Schedule Policy  3	2	[{"changed": {"fields": ["name", "repeat_times"]}}]	29	1
10	2018-11-26 15:52:24.710523+00	2	Demo Schedule Policy 2	2	[{"changed": {"fields": ["name"]}}]	29	1
11	2018-11-26 15:52:42.812769+00	acaede8f-1f05-4d9b-a9e2-747d4140eabf	Demo Service key 1	1	[{"added": {}}]	31	1
12	2018-11-26 15:53:22.711098+00	ebc956ad-5f0f-4385-8781-9290e4e06902	Demo Service key 2	1	[{"added": {}}]	31	1
13	2018-11-26 15:53:55.265137+00	2b1e704d-616d-48a6-bfbf-a73382c69deb	Demo Service key 3	1	[{"added": {}}]	31	1
14	2018-11-26 15:54:59.716885+00	1a32b4c9-6ce3-4c0f-a734-046b4c8bdf6f	Demo Service 1	1	[{"added": {}}]	31	1
15	2018-11-26 15:55:34.466675+00	1	qwerty1	1	[{"added": {}}]	23	1
16	2018-11-26 15:56:25.069339+00	7bece19f-057e-4db8-b6a4-5275b6c916d9	Demo Service 2	1	[{"added": {}}]	31	1
17	2018-11-26 15:56:29.668895+00	1	Some demo data about this Event	1	[{"added": {}}]	22	1
\.


--
-- Data for Name: django_celery_beat_crontabschedule; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.django_celery_beat_crontabschedule (id, minute, hour, day_of_week, day_of_month, month_of_year, timezone) FROM stdin;
\.


--
-- Data for Name: django_celery_beat_intervalschedule; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.django_celery_beat_intervalschedule (id, every, period) FROM stdin;
\.


--
-- Data for Name: django_celery_beat_periodictask; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.django_celery_beat_periodictask (id, name, task, args, kwargs, queue, exchange, routing_key, expires, enabled, last_run_at, total_run_count, date_changed, description, crontab_id, interval_id, solar_id, one_off, start_time, priority) FROM stdin;
\.


--
-- Data for Name: django_celery_beat_periodictasks; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.django_celery_beat_periodictasks (ident, last_update) FROM stdin;
\.


--
-- Data for Name: django_celery_beat_solarschedule; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.django_celery_beat_solarschedule (id, event, latitude, longitude) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	django_celery_beat	crontabschedule
8	django_celery_beat	intervalschedule
9	django_celery_beat	periodictask
10	django_celery_beat	periodictasks
11	django_celery_beat	solarschedule
12	django_twilio	caller
13	django_twilio	credential
14	schedule	calendar
15	schedule	calendarrelation
16	schedule	event
17	schedule	eventrelation
18	schedule	occurrence
19	schedule	rule
20	accounts	token
21	accounts	userprofile
22	events	eventlog
23	incidents	incident
24	incidents	incidentsilenced
25	notification	schedulednotification
26	notification	usernotificationmethod
27	policies	schedulepolicy
28	policies	schedulepolicyrule
29	schedules	schedulepolicy
30	schedules	schedulepolicyrule
31	services	service
32	services	servicesilenced
33	services	servicetokens
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2018-11-26 15:45:51.513256+00
2	auth	0001_initial	2018-11-26 15:45:51.562741+00
3	accounts	0001_initial	2018-11-26 15:45:51.584505+00
4	admin	0001_initial	2018-11-26 15:45:51.604136+00
5	admin	0002_logentry_remove_auto_add	2018-11-26 15:45:51.614424+00
6	admin	0003_logentry_add_action_flag_choices	2018-11-26 15:45:51.625778+00
7	contenttypes	0002_remove_content_type_name	2018-11-26 15:45:51.647429+00
8	auth	0002_alter_permission_name_max_length	2018-11-26 15:45:51.656208+00
9	auth	0003_alter_user_email_max_length	2018-11-26 15:45:51.670576+00
10	auth	0004_alter_user_username_opts	2018-11-26 15:45:51.683979+00
11	auth	0005_alter_user_last_login_null	2018-11-26 15:45:51.697653+00
12	auth	0006_require_contenttypes_0002	2018-11-26 15:45:51.701093+00
13	auth	0007_alter_validators_add_error_messages	2018-11-26 15:45:51.714895+00
14	auth	0008_alter_user_username_max_length	2018-11-26 15:45:51.728984+00
15	auth	0009_alter_user_last_name_max_length	2018-11-26 15:45:51.7415+00
16	django_celery_beat	0001_initial	2018-11-26 15:45:51.766358+00
17	django_celery_beat	0002_auto_20161118_0346	2018-11-26 15:45:51.787418+00
18	django_celery_beat	0003_auto_20161209_0049	2018-11-26 15:45:51.797503+00
19	django_celery_beat	0004_auto_20170221_0000	2018-11-26 15:45:51.803083+00
20	django_celery_beat	0005_add_solarschedule_events_choices	2018-11-26 15:45:51.856984+00
21	django_celery_beat	0006_auto_20180210_1226	2018-11-26 15:45:51.859402+00
22	django_celery_beat	0006_auto_20180322_0932	2018-11-26 15:45:51.861571+00
23	django_celery_beat	0007_auto_20180521_0826	2018-11-26 15:45:51.863476+00
24	django_celery_beat	0008_auto_20180914_1922	2018-11-26 15:45:51.865298+00
25	django_celery_beat	0006_periodictask_priority	2018-11-26 15:45:51.873079+00
26	django_twilio	0001_initial	2018-11-26 15:45:51.89176+00
27	schedule	0001_initial	2018-11-26 15:45:51.982155+00
28	schedule	0002_event_color_event	2018-11-26 15:45:51.999265+00
29	schedule	0003_auto_20160715_0028	2018-11-26 15:45:52.074564+00
30	schedule	0006_update_text_fields_empty_string	2018-11-26 15:45:52.099369+00
31	schedule	0004_text_fields_not_null	2018-11-26 15:45:52.216259+00
32	schedule	0005_verbose_name_plural_for_calendar	2018-11-26 15:45:52.22168+00
33	schedule	0007_merge_text_fields	2018-11-26 15:45:52.224221+00
34	schedule	0008_gfk_index	2018-11-26 15:45:52.261259+00
35	schedule	0008_calendar_slug_unique	2018-11-26 15:45:52.284912+00
36	schedule	0009_merge_20180108_2303	2018-11-26 15:45:52.287957+00
37	schedule	0010_events_set_missing_calendar	2018-11-26 15:45:52.308071+00
38	schedule	0011_event_calendar_not_null	2018-11-26 15:45:52.328782+00
39	schedules	0001_initial	2018-11-26 15:45:52.360316+00
40	services	0001_initial	2018-11-26 15:45:52.415879+00
41	incidents	0001_initial	2018-11-26 15:45:52.429748+00
42	incidents	0002_auto_20181122_1103	2018-11-26 15:45:52.47447+00
43	events	0001_initial	2018-11-26 15:45:52.502813+00
44	notification	0001_initial	2018-11-26 15:45:52.551835+00
45	policies	0001_initial	2018-11-26 15:45:52.58676+00
46	sessions	0001_initial	2018-11-26 15:45:52.596207+00
47	django_celery_beat	0005_add_solarschedule_events_choices_squashed_0009_merge_20181012_1416	2018-11-26 15:45:52.601528+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
wi5hq96qyybnfscbmeoltloladamccci	MTcwMWYwYWMzNDJlMmVjNzI1OTJmMjhmNDUxMmNjOGNjNjFkNTZiNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiYjlkMTUxOTc0OWQ5YjJhZTNjMWU2ZTE0MDM5YWY0NzdkZjA0YmVkIn0=	2018-12-10 15:48:24.842362+00
\.


--
-- Data for Name: django_twilio_caller; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.django_twilio_caller (id, blacklisted, phone_number) FROM stdin;
1	f	+41764744645
\.


--
-- Data for Name: django_twilio_credential; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.django_twilio_credential (id, name, account_sid, auth_token, user_id) FROM stdin;
1	demo	qwertyuiop	qwertyuiop	1
\.


--
-- Data for Name: events_eventlog; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.events_eventlog (id, action, data, occurred_at, incident_key_id, service_key_id, user_id) FROM stdin;
1	log	Some demo data about this Event	2018-11-26 15:55:40+00	1	7bece19f-057e-4db8-b6a4-5275b6c916d9	1
\.


--
-- Data for Name: incidents_incident; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.incidents_incident (id, incident_key, event_type, description, details, occurred_at, service_key_id, service_to_escalate_to_id) FROM stdin;
1	qwerty1	acknowledge	Demo Description Service 1	Demo Details Service 1	2018-11-26 15:54:39+00	acaede8f-1f05-4d9b-a9e2-747d4140eabf	1a32b4c9-6ce3-4c0f-a734-046b4c8bdf6f
\.


--
-- Data for Name: incidents_incidentsilenced; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.incidents_incidentsilenced (id, silenced, silenced_until, incident_id) FROM stdin;
\.


--
-- Data for Name: openduty_schedulednotification; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.openduty_schedulednotification (id, notifier, message, send_at, incident_id, user_to_notify_id) FROM stdin;
\.


--
-- Data for Name: openduty_usernotificationmethod; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.openduty_usernotificationmethod (id, "position", method, user_id) FROM stdin;
\.


--
-- Data for Name: policies_schedulepolicy; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.policies_schedulepolicy (id, name, repeat_times) FROM stdin;
\.


--
-- Data for Name: policies_schedulepolicyrule; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.policies_schedulepolicyrule (id, "position", escalate_after, group_id_id, schedule_id, schedule_policy_id, user_id_id) FROM stdin;
\.


--
-- Data for Name: schedule_calendar; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.schedule_calendar (id, name, slug) FROM stdin;
1	Demo	demo-1
\.


--
-- Data for Name: schedule_calendarrelation; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.schedule_calendarrelation (id, object_id, distinction, inheritable, calendar_id, content_type_id) FROM stdin;
\.


--
-- Data for Name: schedule_event; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.schedule_event (id, start, "end", title, description, created_on, updated_on, end_recurring_period, calendar_id, creator_id, rule_id, color_event) FROM stdin;
\.


--
-- Data for Name: schedule_eventrelation; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.schedule_eventrelation (id, object_id, distinction, content_type_id, event_id) FROM stdin;
\.


--
-- Data for Name: schedule_occurrence; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.schedule_occurrence (id, title, description, start, "end", cancelled, original_start, original_end, created_on, updated_on, event_id) FROM stdin;
\.


--
-- Data for Name: schedule_rule; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.schedule_rule (id, name, description, frequency, params) FROM stdin;
\.


--
-- Data for Name: schedules_schedulepolicy; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.schedules_schedulepolicy (id, name, repeat_times) FROM stdin;
1	Demo Schedule Policy 1	3
3	Demo Schedule Policy  3	3
2	Demo Schedule Policy 2	2
\.


--
-- Data for Name: schedules_schedulepolicyrule; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.schedules_schedulepolicyrule (id, "position", escalate_after, group_id_id, schedule_id, schedule_policy_id, user_id_id) FROM stdin;
\.


--
-- Data for Name: services_service; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.services_service (name, id, retry, escalate_after, notifications_disabled, send_resolve_enabled, policy_id) FROM stdin;
Demo Service key 2	ebc956ad-5f0f-4385-8781-9290e4e06902	2	-1	t	f	2
Demo Service key 3	2b1e704d-616d-48a6-bfbf-a73382c69deb	3	4	f	t	3
Demo Service 2	7bece19f-057e-4db8-b6a4-5275b6c916d9	3	3	f	t	2
Demo Service 1	1a32b4c9-6ce3-4c0f-a734-046b4c8bdf6f	3	1	f	t	1
Demo Service key 1	acaede8f-1f05-4d9b-a9e2-747d4140eabf	3	2	f	t	2
\.


--
-- Data for Name: services_servicesilenced; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.services_servicesilenced (id, silenced, silenced_until, service_id) FROM stdin;
\.


--
-- Data for Name: services_servicetokens; Type: TABLE DATA; Schema: public; Owner: openduty
--

COPY public.services_servicetokens (id, name, service_id_id, token_id_id) FROM stdin;
1		1a32b4c9-6ce3-4c0f-a734-046b4c8bdf6f	4bb275bcb4ca991da2dff78e548278c890ed6f96
2		acaede8f-1f05-4d9b-a9e2-747d4140eabf	cda95a1a396ddf028d040355a534e746e980ce6d
3		acaede8f-1f05-4d9b-a9e2-747d4140eabf	0aa8fe734605e984500df39f756fc925af1b46e4
\.


--
-- Name: accounts_userprofile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.accounts_userprofile_id_seq', 1, true);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


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

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 17, true);


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

SELECT pg_catalog.setval('public.django_twilio_caller_id_seq', 1, true);


--
-- Name: django_twilio_credential_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.django_twilio_credential_id_seq', 1, true);


--
-- Name: events_eventlog_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.events_eventlog_id_seq', 1, true);


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

SELECT pg_catalog.setval('public.policies_schedulepolicy_id_seq', 1, false);


--
-- Name: policies_schedulepolicyrule_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.policies_schedulepolicyrule_id_seq', 1, false);


--
-- Name: schedule_calendar_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.schedule_calendar_id_seq', 1, true);


--
-- Name: schedule_calendarrelation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.schedule_calendarrelation_id_seq', 1, false);


--
-- Name: schedule_event_id_seq; Type: SEQUENCE SET; Schema: public; Owner: openduty
--

SELECT pg_catalog.setval('public.schedule_event_id_seq', 1, false);


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

SELECT pg_catalog.setval('public.schedule_rule_id_seq', 1, false);


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
-- Name: accounts_token accounts_token_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.accounts_token
    ADD CONSTRAINT accounts_token_pkey PRIMARY KEY (key);


--
-- Name: accounts_userprofile accounts_userprofile_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.accounts_userprofile
    ADD CONSTRAINT accounts_userprofile_pkey PRIMARY KEY (id);


--
-- Name: accounts_userprofile accounts_userprofile_user_id_key; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.accounts_userprofile
    ADD CONSTRAINT accounts_userprofile_user_id_key UNIQUE (user_id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_celery_beat_crontabschedule django_celery_beat_crontabschedule_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_celery_beat_crontabschedule
    ADD CONSTRAINT django_celery_beat_crontabschedule_pkey PRIMARY KEY (id);


--
-- Name: django_celery_beat_intervalschedule django_celery_beat_intervalschedule_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_celery_beat_intervalschedule
    ADD CONSTRAINT django_celery_beat_intervalschedule_pkey PRIMARY KEY (id);


--
-- Name: django_celery_beat_periodictask django_celery_beat_periodictask_name_key; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_celery_beat_periodictask
    ADD CONSTRAINT django_celery_beat_periodictask_name_key UNIQUE (name);


--
-- Name: django_celery_beat_periodictask django_celery_beat_periodictask_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_celery_beat_periodictask
    ADD CONSTRAINT django_celery_beat_periodictask_pkey PRIMARY KEY (id);


--
-- Name: django_celery_beat_periodictasks django_celery_beat_periodictasks_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_celery_beat_periodictasks
    ADD CONSTRAINT django_celery_beat_periodictasks_pkey PRIMARY KEY (ident);


--
-- Name: django_celery_beat_solarschedule django_celery_beat_solar_event_latitude_longitude_ba64999a_uniq; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_celery_beat_solarschedule
    ADD CONSTRAINT django_celery_beat_solar_event_latitude_longitude_ba64999a_uniq UNIQUE (event, latitude, longitude);


--
-- Name: django_celery_beat_solarschedule django_celery_beat_solarschedule_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_celery_beat_solarschedule
    ADD CONSTRAINT django_celery_beat_solarschedule_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_twilio_caller django_twilio_caller_phone_number_key; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_twilio_caller
    ADD CONSTRAINT django_twilio_caller_phone_number_key UNIQUE (phone_number);


--
-- Name: django_twilio_caller django_twilio_caller_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_twilio_caller
    ADD CONSTRAINT django_twilio_caller_pkey PRIMARY KEY (id);


--
-- Name: django_twilio_credential django_twilio_credential_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_twilio_credential
    ADD CONSTRAINT django_twilio_credential_pkey PRIMARY KEY (id);


--
-- Name: django_twilio_credential django_twilio_credential_user_id_key; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_twilio_credential
    ADD CONSTRAINT django_twilio_credential_user_id_key UNIQUE (user_id);


--
-- Name: events_eventlog events_eventlog_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.events_eventlog
    ADD CONSTRAINT events_eventlog_pkey PRIMARY KEY (id);


--
-- Name: incidents_incident incidents_incident_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.incidents_incident
    ADD CONSTRAINT incidents_incident_pkey PRIMARY KEY (id);


--
-- Name: incidents_incident incidents_incident_service_key_id_incident_key_f24e88d5_uniq; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.incidents_incident
    ADD CONSTRAINT incidents_incident_service_key_id_incident_key_f24e88d5_uniq UNIQUE (service_key_id, incident_key);


--
-- Name: incidents_incidentsilenced incidents_incidentsilenced_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.incidents_incidentsilenced
    ADD CONSTRAINT incidents_incidentsilenced_pkey PRIMARY KEY (id);


--
-- Name: openduty_schedulednotification openduty_schedulednotification_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.openduty_schedulednotification
    ADD CONSTRAINT openduty_schedulednotification_pkey PRIMARY KEY (id);


--
-- Name: openduty_usernotificationmethod openduty_usernotificationmethod_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.openduty_usernotificationmethod
    ADD CONSTRAINT openduty_usernotificationmethod_pkey PRIMARY KEY (id);


--
-- Name: policies_schedulepolicy policies_schedulepolicy_name_key; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.policies_schedulepolicy
    ADD CONSTRAINT policies_schedulepolicy_name_key UNIQUE (name);


--
-- Name: policies_schedulepolicy policies_schedulepolicy_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.policies_schedulepolicy
    ADD CONSTRAINT policies_schedulepolicy_pkey PRIMARY KEY (id);


--
-- Name: policies_schedulepolicyrule policies_schedulepolicyrule_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.policies_schedulepolicyrule
    ADD CONSTRAINT policies_schedulepolicyrule_pkey PRIMARY KEY (id);


--
-- Name: schedule_calendar schedule_calendar_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedule_calendar
    ADD CONSTRAINT schedule_calendar_pkey PRIMARY KEY (id);


--
-- Name: schedule_calendar schedule_calendar_slug_ba17e861_uniq; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedule_calendar
    ADD CONSTRAINT schedule_calendar_slug_ba17e861_uniq UNIQUE (slug);


--
-- Name: schedule_calendarrelation schedule_calendarrelation_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedule_calendarrelation
    ADD CONSTRAINT schedule_calendarrelation_pkey PRIMARY KEY (id);


--
-- Name: schedule_event schedule_event_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedule_event
    ADD CONSTRAINT schedule_event_pkey PRIMARY KEY (id);


--
-- Name: schedule_eventrelation schedule_eventrelation_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedule_eventrelation
    ADD CONSTRAINT schedule_eventrelation_pkey PRIMARY KEY (id);


--
-- Name: schedule_occurrence schedule_occurrence_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedule_occurrence
    ADD CONSTRAINT schedule_occurrence_pkey PRIMARY KEY (id);


--
-- Name: schedule_rule schedule_rule_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedule_rule
    ADD CONSTRAINT schedule_rule_pkey PRIMARY KEY (id);


--
-- Name: schedules_schedulepolicy schedules_schedulepolicy_name_key; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedules_schedulepolicy
    ADD CONSTRAINT schedules_schedulepolicy_name_key UNIQUE (name);


--
-- Name: schedules_schedulepolicy schedules_schedulepolicy_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedules_schedulepolicy
    ADD CONSTRAINT schedules_schedulepolicy_pkey PRIMARY KEY (id);


--
-- Name: schedules_schedulepolicyrule schedules_schedulepolicyrule_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedules_schedulepolicyrule
    ADD CONSTRAINT schedules_schedulepolicyrule_pkey PRIMARY KEY (id);


--
-- Name: services_service services_service_name_key; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.services_service
    ADD CONSTRAINT services_service_name_key UNIQUE (name);


--
-- Name: services_service services_service_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.services_service
    ADD CONSTRAINT services_service_pkey PRIMARY KEY (id);


--
-- Name: services_servicesilenced services_servicesilenced_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.services_servicesilenced
    ADD CONSTRAINT services_servicesilenced_pkey PRIMARY KEY (id);


--
-- Name: services_servicetokens services_servicetokens_pkey; Type: CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.services_servicetokens
    ADD CONSTRAINT services_servicetokens_pkey PRIMARY KEY (id);


--
-- Name: accounts_token_key_56c4ebe2_like; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX accounts_token_key_56c4ebe2_like ON public.accounts_token USING btree (key varchar_pattern_ops);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_celery_beat_periodictask_crontab_id_d3cba168; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX django_celery_beat_periodictask_crontab_id_d3cba168 ON public.django_celery_beat_periodictask USING btree (crontab_id);


--
-- Name: django_celery_beat_periodictask_interval_id_a8ca27da; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX django_celery_beat_periodictask_interval_id_a8ca27da ON public.django_celery_beat_periodictask USING btree (interval_id);


--
-- Name: django_celery_beat_periodictask_name_265a36b7_like; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX django_celery_beat_periodictask_name_265a36b7_like ON public.django_celery_beat_periodictask USING btree (name varchar_pattern_ops);


--
-- Name: django_celery_beat_periodictask_solar_id_a87ce72c; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX django_celery_beat_periodictask_solar_id_a87ce72c ON public.django_celery_beat_periodictask USING btree (solar_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: django_twilio_caller_phone_number_6a9cca42_like; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX django_twilio_caller_phone_number_6a9cca42_like ON public.django_twilio_caller USING btree (phone_number varchar_pattern_ops);


--
-- Name: events_eventlog_incident_key_id_112fa9f1; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX events_eventlog_incident_key_id_112fa9f1 ON public.events_eventlog USING btree (incident_key_id);


--
-- Name: events_eventlog_service_key_id_ab1b91b0; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX events_eventlog_service_key_id_ab1b91b0 ON public.events_eventlog USING btree (service_key_id);


--
-- Name: events_eventlog_user_id_14b971e8; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX events_eventlog_user_id_14b971e8 ON public.events_eventlog USING btree (user_id);


--
-- Name: incidents_incident_service_key_id_018cbe1e; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX incidents_incident_service_key_id_018cbe1e ON public.incidents_incident USING btree (service_key_id);


--
-- Name: incidents_incident_service_to_escalate_to_id_85b29129; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX incidents_incident_service_to_escalate_to_id_85b29129 ON public.incidents_incident USING btree (service_to_escalate_to_id);


--
-- Name: incidents_incidentsilenced_incident_id_8f85c2cf; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX incidents_incidentsilenced_incident_id_8f85c2cf ON public.incidents_incidentsilenced USING btree (incident_id);


--
-- Name: openduty_schedulednotification_incident_id_cae9b356; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX openduty_schedulednotification_incident_id_cae9b356 ON public.openduty_schedulednotification USING btree (incident_id);


--
-- Name: openduty_schedulednotification_user_to_notify_id_d49e6014; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX openduty_schedulednotification_user_to_notify_id_d49e6014 ON public.openduty_schedulednotification USING btree (user_to_notify_id);


--
-- Name: openduty_usernotificationmethod_user_id_73db7053; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX openduty_usernotificationmethod_user_id_73db7053 ON public.openduty_usernotificationmethod USING btree (user_id);


--
-- Name: policies_schedulepolicy_name_9dc89b96_like; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX policies_schedulepolicy_name_9dc89b96_like ON public.policies_schedulepolicy USING btree (name varchar_pattern_ops);


--
-- Name: policies_schedulepolicyrule_group_id_id_e5fed0e0; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX policies_schedulepolicyrule_group_id_id_e5fed0e0 ON public.policies_schedulepolicyrule USING btree (group_id_id);


--
-- Name: policies_schedulepolicyrule_schedule_id_3492fa23; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX policies_schedulepolicyrule_schedule_id_3492fa23 ON public.policies_schedulepolicyrule USING btree (schedule_id);


--
-- Name: policies_schedulepolicyrule_schedule_policy_id_b234d218; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX policies_schedulepolicyrule_schedule_policy_id_b234d218 ON public.policies_schedulepolicyrule USING btree (schedule_policy_id);


--
-- Name: policies_schedulepolicyrule_user_id_id_1fdd66d1; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX policies_schedulepolicyrule_user_id_id_1fdd66d1 ON public.policies_schedulepolicyrule USING btree (user_id_id);


--
-- Name: schedule_calendar_slug_ba17e861_like; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX schedule_calendar_slug_ba17e861_like ON public.schedule_calendar USING btree (slug varchar_pattern_ops);


--
-- Name: schedule_calendarrelatio_content_type_id_object_i_3378a516_idx; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX schedule_calendarrelatio_content_type_id_object_i_3378a516_idx ON public.schedule_calendarrelation USING btree (content_type_id, object_id);


--
-- Name: schedule_calendarrelation_calendar_id_0a50be2e; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX schedule_calendarrelation_calendar_id_0a50be2e ON public.schedule_calendarrelation USING btree (calendar_id);


--
-- Name: schedule_calendarrelation_content_type_id_f2a42f5b; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX schedule_calendarrelation_content_type_id_f2a42f5b ON public.schedule_calendarrelation USING btree (content_type_id);


--
-- Name: schedule_calendarrelation_object_id_1743bce6; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX schedule_calendarrelation_object_id_1743bce6 ON public.schedule_calendarrelation USING btree (object_id);


--
-- Name: schedule_event_calendar_id_eb1c700f; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX schedule_event_calendar_id_eb1c700f ON public.schedule_event USING btree (calendar_id);


--
-- Name: schedule_event_creator_id_d2ffab6e; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX schedule_event_creator_id_d2ffab6e ON public.schedule_event USING btree (creator_id);


--
-- Name: schedule_event_end_674c5848; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX schedule_event_end_674c5848 ON public.schedule_event USING btree ("end");


--
-- Name: schedule_event_end_recurring_period_672addcf; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX schedule_event_end_recurring_period_672addcf ON public.schedule_event USING btree (end_recurring_period);


--
-- Name: schedule_event_rule_id_90b83d31; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX schedule_event_rule_id_90b83d31 ON public.schedule_event USING btree (rule_id);


--
-- Name: schedule_event_start_a11492a7; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX schedule_event_start_a11492a7 ON public.schedule_event USING btree (start);


--
-- Name: schedule_event_start_end_89f30672_idx; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX schedule_event_start_end_89f30672_idx ON public.schedule_event USING btree (start, "end");


--
-- Name: schedule_eventrelation_content_type_id_d4187723; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX schedule_eventrelation_content_type_id_d4187723 ON public.schedule_eventrelation USING btree (content_type_id);


--
-- Name: schedule_eventrelation_content_type_id_object_id_c1b1e893_idx; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX schedule_eventrelation_content_type_id_object_id_c1b1e893_idx ON public.schedule_eventrelation USING btree (content_type_id, object_id);


--
-- Name: schedule_eventrelation_event_id_8c57a7b4; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX schedule_eventrelation_event_id_8c57a7b4 ON public.schedule_eventrelation USING btree (event_id);


--
-- Name: schedule_eventrelation_object_id_e22334a2; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX schedule_eventrelation_object_id_e22334a2 ON public.schedule_eventrelation USING btree (object_id);


--
-- Name: schedule_occurrence_end_ae255624; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX schedule_occurrence_end_ae255624 ON public.schedule_occurrence USING btree ("end");


--
-- Name: schedule_occurrence_event_id_ade47cd8; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX schedule_occurrence_event_id_ade47cd8 ON public.schedule_occurrence USING btree (event_id);


--
-- Name: schedule_occurrence_start_b28eeb2f; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX schedule_occurrence_start_b28eeb2f ON public.schedule_occurrence USING btree (start);


--
-- Name: schedule_occurrence_start_end_5fc98870_idx; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX schedule_occurrence_start_end_5fc98870_idx ON public.schedule_occurrence USING btree (start, "end");


--
-- Name: schedules_schedulepolicy_name_fa7d63d0_like; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX schedules_schedulepolicy_name_fa7d63d0_like ON public.schedules_schedulepolicy USING btree (name varchar_pattern_ops);


--
-- Name: schedules_schedulepolicyrule_group_id_id_4478a36a; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX schedules_schedulepolicyrule_group_id_id_4478a36a ON public.schedules_schedulepolicyrule USING btree (group_id_id);


--
-- Name: schedules_schedulepolicyrule_schedule_id_806c909a; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX schedules_schedulepolicyrule_schedule_id_806c909a ON public.schedules_schedulepolicyrule USING btree (schedule_id);


--
-- Name: schedules_schedulepolicyrule_schedule_policy_id_40631897; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX schedules_schedulepolicyrule_schedule_policy_id_40631897 ON public.schedules_schedulepolicyrule USING btree (schedule_policy_id);


--
-- Name: schedules_schedulepolicyrule_user_id_id_8d1465ae; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX schedules_schedulepolicyrule_user_id_id_8d1465ae ON public.schedules_schedulepolicyrule USING btree (user_id_id);


--
-- Name: services_service_name_22a0ef31_like; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX services_service_name_22a0ef31_like ON public.services_service USING btree (name varchar_pattern_ops);


--
-- Name: services_service_policy_id_98b62acc; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX services_service_policy_id_98b62acc ON public.services_service USING btree (policy_id);


--
-- Name: services_servicesilenced_service_id_ed23f28e; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX services_servicesilenced_service_id_ed23f28e ON public.services_servicesilenced USING btree (service_id);


--
-- Name: services_servicetokens_service_id_id_aca771d6; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX services_servicetokens_service_id_id_aca771d6 ON public.services_servicetokens USING btree (service_id_id);


--
-- Name: services_servicetokens_token_id_id_088f8110; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX services_servicetokens_token_id_id_088f8110 ON public.services_servicetokens USING btree (token_id_id);


--
-- Name: services_servicetokens_token_id_id_088f8110_like; Type: INDEX; Schema: public; Owner: openduty
--

CREATE INDEX services_servicetokens_token_id_id_088f8110_like ON public.services_servicetokens USING btree (token_id_id varchar_pattern_ops);


--
-- Name: accounts_userprofile accounts_userprofile_user_id_92240672_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.accounts_userprofile
    ADD CONSTRAINT accounts_userprofile_user_id_92240672_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_celery_beat_periodictask django_celery_beat_p_crontab_id_d3cba168_fk_django_ce; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_celery_beat_periodictask
    ADD CONSTRAINT django_celery_beat_p_crontab_id_d3cba168_fk_django_ce FOREIGN KEY (crontab_id) REFERENCES public.django_celery_beat_crontabschedule(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_celery_beat_periodictask django_celery_beat_p_interval_id_a8ca27da_fk_django_ce; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_celery_beat_periodictask
    ADD CONSTRAINT django_celery_beat_p_interval_id_a8ca27da_fk_django_ce FOREIGN KEY (interval_id) REFERENCES public.django_celery_beat_intervalschedule(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_celery_beat_periodictask django_celery_beat_p_solar_id_a87ce72c_fk_django_ce; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_celery_beat_periodictask
    ADD CONSTRAINT django_celery_beat_p_solar_id_a87ce72c_fk_django_ce FOREIGN KEY (solar_id) REFERENCES public.django_celery_beat_solarschedule(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_twilio_credential django_twilio_credential_user_id_29c9a22d_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.django_twilio_credential
    ADD CONSTRAINT django_twilio_credential_user_id_29c9a22d_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: events_eventlog events_eventlog_incident_key_id_112fa9f1_fk_incidents; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.events_eventlog
    ADD CONSTRAINT events_eventlog_incident_key_id_112fa9f1_fk_incidents FOREIGN KEY (incident_key_id) REFERENCES public.incidents_incident(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: events_eventlog events_eventlog_service_key_id_ab1b91b0_fk_services_service_id; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.events_eventlog
    ADD CONSTRAINT events_eventlog_service_key_id_ab1b91b0_fk_services_service_id FOREIGN KEY (service_key_id) REFERENCES public.services_service(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: events_eventlog events_eventlog_user_id_14b971e8_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.events_eventlog
    ADD CONSTRAINT events_eventlog_user_id_14b971e8_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: incidents_incident incidents_incident_service_key_id_018cbe1e_fk_services_; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.incidents_incident
    ADD CONSTRAINT incidents_incident_service_key_id_018cbe1e_fk_services_ FOREIGN KEY (service_key_id) REFERENCES public.services_service(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: incidents_incident incidents_incident_service_to_escalate__85b29129_fk_services_; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.incidents_incident
    ADD CONSTRAINT incidents_incident_service_to_escalate__85b29129_fk_services_ FOREIGN KEY (service_to_escalate_to_id) REFERENCES public.services_service(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: incidents_incidentsilenced incidents_incidentsi_incident_id_8f85c2cf_fk_incidents; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.incidents_incidentsilenced
    ADD CONSTRAINT incidents_incidentsi_incident_id_8f85c2cf_fk_incidents FOREIGN KEY (incident_id) REFERENCES public.incidents_incident(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: openduty_schedulednotification openduty_scheduledno_incident_id_cae9b356_fk_incidents; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.openduty_schedulednotification
    ADD CONSTRAINT openduty_scheduledno_incident_id_cae9b356_fk_incidents FOREIGN KEY (incident_id) REFERENCES public.incidents_incident(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: openduty_schedulednotification openduty_scheduledno_user_to_notify_id_d49e6014_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.openduty_schedulednotification
    ADD CONSTRAINT openduty_scheduledno_user_to_notify_id_d49e6014_fk_auth_user FOREIGN KEY (user_to_notify_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: openduty_usernotificationmethod openduty_usernotific_user_id_73db7053_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.openduty_usernotificationmethod
    ADD CONSTRAINT openduty_usernotific_user_id_73db7053_fk_auth_user FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: policies_schedulepolicyrule policies_schedulepol_group_id_id_e5fed0e0_fk_auth_grou; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.policies_schedulepolicyrule
    ADD CONSTRAINT policies_schedulepol_group_id_id_e5fed0e0_fk_auth_grou FOREIGN KEY (group_id_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: policies_schedulepolicyrule policies_schedulepol_schedule_id_3492fa23_fk_schedule_; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.policies_schedulepolicyrule
    ADD CONSTRAINT policies_schedulepol_schedule_id_3492fa23_fk_schedule_ FOREIGN KEY (schedule_id) REFERENCES public.schedule_calendar(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: policies_schedulepolicyrule policies_schedulepol_schedule_policy_id_b234d218_fk_policies_; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.policies_schedulepolicyrule
    ADD CONSTRAINT policies_schedulepol_schedule_policy_id_b234d218_fk_policies_ FOREIGN KEY (schedule_policy_id) REFERENCES public.policies_schedulepolicy(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: policies_schedulepolicyrule policies_schedulepolicyrule_user_id_id_1fdd66d1_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.policies_schedulepolicyrule
    ADD CONSTRAINT policies_schedulepolicyrule_user_id_id_1fdd66d1_fk_auth_user_id FOREIGN KEY (user_id_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: schedule_calendarrelation schedule_calendarrel_calendar_id_0a50be2e_fk_schedule_; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedule_calendarrelation
    ADD CONSTRAINT schedule_calendarrel_calendar_id_0a50be2e_fk_schedule_ FOREIGN KEY (calendar_id) REFERENCES public.schedule_calendar(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: schedule_calendarrelation schedule_calendarrel_content_type_id_f2a42f5b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedule_calendarrelation
    ADD CONSTRAINT schedule_calendarrel_content_type_id_f2a42f5b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: schedule_event schedule_event_calendar_id_eb1c700f_fk_schedule_calendar_id; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedule_event
    ADD CONSTRAINT schedule_event_calendar_id_eb1c700f_fk_schedule_calendar_id FOREIGN KEY (calendar_id) REFERENCES public.schedule_calendar(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: schedule_event schedule_event_creator_id_d2ffab6e_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedule_event
    ADD CONSTRAINT schedule_event_creator_id_d2ffab6e_fk_auth_user_id FOREIGN KEY (creator_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: schedule_event schedule_event_rule_id_90b83d31_fk_schedule_rule_id; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedule_event
    ADD CONSTRAINT schedule_event_rule_id_90b83d31_fk_schedule_rule_id FOREIGN KEY (rule_id) REFERENCES public.schedule_rule(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: schedule_eventrelation schedule_eventrelati_content_type_id_d4187723_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedule_eventrelation
    ADD CONSTRAINT schedule_eventrelati_content_type_id_d4187723_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: schedule_eventrelation schedule_eventrelation_event_id_8c57a7b4_fk_schedule_event_id; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedule_eventrelation
    ADD CONSTRAINT schedule_eventrelation_event_id_8c57a7b4_fk_schedule_event_id FOREIGN KEY (event_id) REFERENCES public.schedule_event(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: schedule_occurrence schedule_occurrence_event_id_ade47cd8_fk_schedule_event_id; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedule_occurrence
    ADD CONSTRAINT schedule_occurrence_event_id_ade47cd8_fk_schedule_event_id FOREIGN KEY (event_id) REFERENCES public.schedule_event(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: schedules_schedulepolicyrule schedules_schedulepo_group_id_id_4478a36a_fk_auth_grou; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedules_schedulepolicyrule
    ADD CONSTRAINT schedules_schedulepo_group_id_id_4478a36a_fk_auth_grou FOREIGN KEY (group_id_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: schedules_schedulepolicyrule schedules_schedulepo_schedule_id_806c909a_fk_schedule_; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedules_schedulepolicyrule
    ADD CONSTRAINT schedules_schedulepo_schedule_id_806c909a_fk_schedule_ FOREIGN KEY (schedule_id) REFERENCES public.schedule_calendar(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: schedules_schedulepolicyrule schedules_schedulepo_schedule_policy_id_40631897_fk_schedules; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedules_schedulepolicyrule
    ADD CONSTRAINT schedules_schedulepo_schedule_policy_id_40631897_fk_schedules FOREIGN KEY (schedule_policy_id) REFERENCES public.schedules_schedulepolicy(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: schedules_schedulepolicyrule schedules_schedulepo_user_id_id_8d1465ae_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.schedules_schedulepolicyrule
    ADD CONSTRAINT schedules_schedulepo_user_id_id_8d1465ae_fk_auth_user FOREIGN KEY (user_id_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: services_service services_service_policy_id_98b62acc_fk_schedules; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.services_service
    ADD CONSTRAINT services_service_policy_id_98b62acc_fk_schedules FOREIGN KEY (policy_id) REFERENCES public.schedules_schedulepolicy(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: services_servicesilenced services_servicesile_service_id_ed23f28e_fk_services_; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.services_servicesilenced
    ADD CONSTRAINT services_servicesile_service_id_ed23f28e_fk_services_ FOREIGN KEY (service_id) REFERENCES public.services_service(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: services_servicetokens services_servicetoke_service_id_id_aca771d6_fk_services_; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.services_servicetokens
    ADD CONSTRAINT services_servicetoke_service_id_id_aca771d6_fk_services_ FOREIGN KEY (service_id_id) REFERENCES public.services_service(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: services_servicetokens services_servicetoke_token_id_id_088f8110_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: openduty
--

ALTER TABLE ONLY public.services_servicetokens
    ADD CONSTRAINT services_servicetoke_token_id_id_088f8110_fk_accounts_ FOREIGN KEY (token_id_id) REFERENCES public.accounts_token(key) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

