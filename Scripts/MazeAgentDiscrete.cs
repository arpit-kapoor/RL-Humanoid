using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using MLAgents;
using System;

public class MazeAgentDiscrete : Agent
{
    public Transform Target;
    public GameObject mujoco;
    public IntVector2 coordinate;
    private int maze_size;
    string[,] Maze;
    public MJRemote mjr;

    public enum Direction
    {
        None,
        North,
        South,
        East,
        West
    }

    

    // Start is called before the first frame update
    void Start()
    {
        this.transform.position = new Vector3(-6.0f, 1.0f, 2.0f);
        coordinate = new IntVector2(1, 0);
        Target.position = new Vector3(-18.0f, 0.0f, 18.0f);
        maze_size = 5;
        //Height, Width => (z, x)
        //"NSEW"
        Maze = new string[5, 5]{{"1101","1000","1010","1101","1010"},
                                {"1011","0011","0011","1001","0010"},
                                {"0101","0110","0011","0011","0011"},
                                {"1001","1010","0011","0011","0011"},
                                {"0111","0101","0100","0110","0111"}};

//        Debug.Log(GetCellState(coordinate).ToString());

        mjr = mujoco.GetComponent<MJRemote>();

 
    }

    int GetCellState(IntVector2 coordinate)
    {
        int state = 0;
        int x = coordinate.x;
        int z = coordinate.z;
        string cell_state = Maze[z, x];
        state = System.Convert.ToInt32(cell_state, 2);
        return state;
    }

    bool IsSafe(IntVector2 coordinate, int direction)
    {
        int x = coordinate.x;
        int z = coordinate.z;
        string cell_state = Maze[z, x];
        int wall_state = cell_state[direction-1];
//        Debug.Log(wall_state);
        if ((wall_state - '0') == 1) {
//            Debug.Log(false);
            return false;
        }
//        Debug.Log(true);
        return true;
    }

    public override void AgentReset()
    {
        this.transform.position = new Vector3(-6.0f, 1.0f, 2.0f);
        coordinate = new IntVector2(1, 0);
    }

    public override void CollectObservations()
    {
        float[] position = {coordinate.x, coordinate.z}; 
        AddVectorObs((float)coordinate.x);
        AddVectorObs((float)coordinate.z);
    }

    void UpdateState(Direction direction)
    {
        if (direction == Direction.North)
        {
            coordinate.z -= 1;
            this.transform.position += new Vector3(0.0f, 0.0f, -4.0f);
        }
            
        else if (direction == Direction.South)
        {
            coordinate.z += 1;
            this.transform.position += new Vector3(0.0f, 0.0f, 4.0f);
        }
            
        else if (direction == Direction.East)
        {
            coordinate.x += 1;
            this.transform.position += new Vector3(-4.0f, 0.0f, 0.0f);
        }

        else if (direction == Direction.West)
        {
            coordinate.x -= 1;
            this.transform.position += new Vector3(4.0f, 0.0f, 0.0f);
        }
    }

    public override void AgentAction(float[] vectorAction, string textAction)
    {
        //Debug.Log(coordinate.x);
        //Debug.Log(coordinate.z);
        int action = (int)vectorAction[0];
        if (action == 0)
            return;
        Direction move = (Direction)action;
        if (IsSafe(coordinate, action))
        {
            UpdateState(move);
        }

//        float distanceToTarget = Vector3.Distance(this.transform.position,Target.position);
        float distanceToTarget = Vector3.Distance(mjr.humanoid_pos.position,Target.position);
        // Reached target
        if (distanceToTarget < 1.42f)
        {
            SetReward(1.0f);
            Done();
        }

        else
        {
            SetReward(-0.1f / (maze_size * maze_size));
        }

        //float timer = 1.0f;
        //while (timer != 0.0f)
        //{
        //    timer -= Time.deltaTime;
        //    Debug.Log(timer);
        //}
    }
    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            Done();
        }

//        Debug.Log(mjr.move_maze);
        if (mjr.move_maze)
        {
            RequestDecision();
            mjr.move_maze = false;
        }
        if (mjr.ag_reset)
        {
            AgentReset();
            mjr.ag_reset = false;
        }
    }
}
