from datetime import timedelta

WORKFLOW_NAME = "daily_infra_brief"
CRON = "0 14 * * 1-5"
SLACK_CHANNEL = "infra-updates"
PROMPT = (
    "Use the infra/on-call overlay. Summarize sample service health, open incidents, "
    "and one recommended next action. Be explicit that this is sample data."
)


async def handler(inp, ctx):
    summary = await ctx.call_tool("infra_status", "health", {})
    result = await ctx.agent_turn(
        f"Write the daily infra sample brief from this data: {summary}"
    )
    await ctx.post_to_slack(SLACK_CHANNEL, result["result_text"])
    await ctx.sleep("cooldown", timedelta(seconds=1))
    return result
