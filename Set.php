<?php

class Set
{
    private $set = [];

    public function contains($key)
    {
        return isset($this->$set[$key]);
    }

    public function add($key)
    {
        $this->set[$key] = true;
    }

    public function remove($key)
    {
        unset($this->set[$key]);
    }
}
