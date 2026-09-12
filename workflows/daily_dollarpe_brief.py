from datetime import timedelta

WORKFLOW_NAME = "daily_dollarpe_brief"
CRON = "0 9 * * 1-5"
SLACK_CHANNEL = "dollarpe-infra"
PROMPT = (
    "You are DollarPe Bot. Summarize sample health for Nebula/Nova/Stargate/Horizon "
    "and open DollarPe incidents, plus one next action. Label sample data clearly."
)


async def handler(inp, ctx):
    summary = await ctx.call_tool("dollarpe_ops", "health", {})
    result = await ctx.agent_turn(
        f"Write the daily DollarPe Bot infra brief from this data: {summary}"
    )
    await ctx.post_to_slack(SLACK_CHANNEL, result["result_text"])
    await ctx.sleep("cooldown", timedelta(seconds=1))
    return result
