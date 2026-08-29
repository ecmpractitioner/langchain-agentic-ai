from pydantic import BaseModel, Field


class Source(BaseModel):
    """Schema for a source used by the agent"""

    url: str = Field(description="The URL of the source")


class AgentResponse(BaseModel):
    """Schema for the agent response"""

    answer: str = Field(description="Agent answer to the query")
    sources: list[Source] = Field(
        description="List sources used to generate the answer", default_factory=list
    )
