using System;
using System.Collections.Generic;

namespace Lab6.Models
{
    public partial class Finance
    {
        public int Id { get; set; }
        public int Action { get; set; }
        public int Sum { get; set; }
        public DateTime Time { get; set; }
    }
}
