# Xunxiashi Template Fields

This file defines the canonical placeholder field schema for all templates.

Use these names consistently when:

- filling templates manually
- generating files from questionnaire answers
- building scripts later

## Naming Rule

All placeholders should be globally unique enough to be recognized without template context.

Use a domain prefix:

- `oc_` for `openclaw.json`
- `user_` for `USER.md`
- `identity_` for `IDENTITY.md`
- `soul_` for `SOUL.md`
- `agent_` for `AGENTS.md`
- `tools_` for `TOOLS.md`
- `heartbeat_` for `HEARTBEAT.md`
- `memory_` for `MEMORY.md`

## `openclaw.json`

- `{{oc_safety_profile}}`

Do not treat startup recovery, new-session recovery, or write-before-remember as native `openclaw.json` fields.
Those behaviors need official OpenClaw hook wiring plus workspace rules.

## `USER.md`

- `{{user_preferred_name}}`
- `{{user_main_role}}`
- `{{user_work_summary}}`
- `{{user_task_1}}`
- `{{user_task_2}}`
- `{{user_task_3}}`
- `{{user_main_burden}}`
- `{{user_main_help_goal}}`
- `{{user_jargon_1}}`
- `{{user_jargon_2}}`
- `{{user_jargon_3}}`
- `{{user_rule_1}}`
- `{{user_rule_2}}`
- `{{user_rule_3}}`

## `IDENTITY.md`

- `{{identity_companion_type}}`
- `{{identity_tone_style}}`
- `{{identity_reply_density}}`
- `{{identity_good_response_feel}}`
- `{{identity_bad_response_feel}}`
- `{{identity_mistake_style}}`
- `{{identity_opening_phrase}}`
- `{{identity_closing_phrase}}`
- `{{identity_light_flavor}}`
- `{{identity_avoid_phrase_1}}`
- `{{identity_avoid_phrase_2}}`
- `{{identity_avoid_phrase_3}}`

## `SOUL.md`

- `{{soul_inner_spirit}}`
- `{{soul_work_temperament}}`
- `{{soul_pressure_behavior}}`
- `{{soul_no_decide_1}}`
- `{{soul_no_decide_2}}`
- `{{soul_risk_default}}`
- `{{soul_uncertainty_default}}`
- `{{soul_interesting_quality}}`
- `{{soul_allowed_humor}}`
- `{{soul_forbidden_inner_style}}`

## `AGENTS.md`

- `{{agent_main_task}}`
- `{{agent_step_1}}`
- `{{agent_step_2}}`
- `{{agent_step_3}}`
- `{{agent_delivery_item_1}}`
- `{{agent_delivery_item_2}}`
- `{{agent_delivery_item_3}}`
- `{{agent_missing_info_rule}}`
- `{{agent_direction_check_rule}}`
- `{{agent_direct_action_rule}}`
- `{{agent_ask_first_rule}}`

## `TOOLS.md`

- `{{tools_search_behavior}}`
- `{{tools_source_pref_1}}`
- `{{tools_source_pref_2}}`
- `{{tools_source_avoid_1}}`
- `{{tools_source_avoid_2}}`
- `{{tools_memory_save_behavior}}`
- `{{tools_memory_read_behavior}}`
- `{{tools_memory_proof_behavior}}`
- `{{tools_high_risk_rule}}`
- `{{tools_external_send_rule}}`
- `{{tools_file_change_rule}}`
- `{{tools_tool_failure_style}}`

## `HEARTBEAT.md`

- `{{heartbeat_proactivity_level}}`
- `{{heartbeat_too_proactive_definition}}`
- `{{heartbeat_startup_notice_style}}`
- `{{heartbeat_new_session_recovery_style}}`
- `{{heartbeat_daily_note_behavior}}`
- `{{heartbeat_rule_promotion_behavior}}`
- `{{heartbeat_repeat_mistake_behavior}}`

## `MEMORY.md`

- `{{memory_durable_pref_1}}`
- `{{memory_durable_pref_2}}`
- `{{memory_durable_pref_3}}`
- `{{memory_durable_rule_1}}`
- `{{memory_durable_rule_2}}`
- `{{memory_durable_rule_3}}`
- `{{memory_durable_fact_1}}`
- `{{memory_durable_fact_2}}`

## Filling Guidance

### Leave blanks only when truly unknown

If a field is unknown:

- infer only when the risk is low
- otherwise leave a clear placeholder for later completion

### Prefer concise values

Template fields should usually be:

- one sentence
- one rule
- one preference

Do not stuff long essays into individual fields.

### Move complexity upward when needed

If a rule is too complex for one field:

- summarize the default in the field
- move the operational detail into the body text or a checklist later
