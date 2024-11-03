import { Sparkles } from "../../components/Sparkles";
import NavBar from "../../components/NavBar";

export default function Dashboard() {
  return (
    <div className="h-screen w-screen overflow-hidden">
      <NavBar />
      <div className="mx-auto mt-96 w-screen max-w-2xl">
        <div className="text-center text-3xl text-white">
          <span className="text-indigo-200">Welcome to...</span>

          <br />
        </div>
      </div>

      <div className="relative -mt-32 h-96 w-screen overflow-hidden [mask-image:radial-gradient(50%_50%,white,transparent)] before:absolute before:inset-0 before:bg-[radial-gradient(circle_at_bottom_center,#8350e8,transparent_70%)] before:opacity-40 after:absolute after:-left-1/2 after:top-1/2 after:aspect-[1/0.7] after:w-[200%] after:rounded-[100%] after:border-t after:border-[#7876c566] after:bg-zinc-900">
        <Sparkles
          density={1500}
          className="absolute inset-x-0 bottom-0 h-full w-full [mask-image:radial-gradient(90%_90%_at_center,white,transparent_100%)]"
        />
      </div>
    </div>
  );
}
