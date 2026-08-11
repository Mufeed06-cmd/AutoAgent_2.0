# AutoAgent 2.0

A modular multi-agent AI system built in Python with planning, memory, and task execution.

## What it does
AutoAgent takes a high-level task, breaks it into subtasks using a Planner, routes each subtask to the right Agent, and executes them with shared memory and state.

## Architecture
```
Main
 ├── Planner         → breaks task into subtasks
 ├── AgentRegistry   → stores and retrieves agents
 ├── TaskExecutor    → routes and executes subtasks
 ├── SharedState     → temporary data during execution (RAM)
 ├── Memory          → persistent data across tasks (DB)
 └── Agents
      ├── CodingAgent
      ├── ResearchAgent
      └── TestingAgent
```

## Project Structure
```
AutoAgent_2.0/
├── agents/          # CodingAgent, ResearchAgent, TestingAgent
├── executor/        # TaskExecutor
├── memory/          # Memory module
├── planner/         # Planner
├── registry/        # AgentRegistry
├── shared_state/    # SharedState
├── tools/           # Tool integrations
├── response_builder/
├── tests/           # pytest unit tests
└── main.py
```

## Run
```bash
python main.py
```

## Run Tests
```bash
python -m pytest
```

## Status
🟡 In active development — Memory behavioral integration complete, end-to-end testing in progress.
