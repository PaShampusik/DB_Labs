using System;
using System.Collections.Generic;

namespace Lab6.Models
{
    public partial class Log
    {
        public int Id { get; set; }
        /// <summary>
        /// 1 - entrance || 0 - exit
        /// </summary>
        public int Action { get; set; }
        public int IdUser { get; set; }

        public virtual User IdUserNavigation { get; set; } = null!;
    }
}
